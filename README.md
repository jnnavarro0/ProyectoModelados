# ProyectoModelados
Universidad de las Fuerzas Armadas ESPE
Departamento de Ciencias de la Computación
Modelado avanzado de base de datos
NRC: 10049
Proyecto Parcial 2
Changoluisa E., Navarro J., Ñacata H.
13 de julio de 2023


Introducción	3
Visión general	4
Objetivos	5
Requerimientos	5
Diseño del Sistema	7
Documentación de Código	8
Pruebas	8
Desarrollo	10
Referencias	19

Introducción

En el ámbito actual de la gestión de datos, las bases de datos distribuidas y las tecnologías NoSQL han adquirido una relevancia considerable. Estas bases de datos brindan soluciones escalables y flexibles para almacenar y procesar grandes volúmenes de información en entornos distribuidos.
Uno de los desafíos principales en la administración de bases de datos distribuidas NoSQL es la integración del proceso Extract, Transform, Load (ETL). El ETL se refiere a un conjunto de técnicas y herramientas utilizadas para extraer datos de diversas fuentes, transformarlos de acuerdo con los requisitos del negocio y cargarlos en un destino final, como una base de datos.
En este proyecto, nos centraremos en explorar y diseñar una solución para la integración del ETL en una base de datos distribuida NoSQL. Nuestro objetivo principal consiste en desarrollar un sistema que permita extraer eficientemente datos de múltiples fuentes, transformarlos para adecuarlos a la estructura y el formato de la base de datos distribuida, y finalmente, cargar exitosamente los datos transformados en dicha base de datos.
Para lograr este objetivo, llevaremos a cabo una investigación de diferentes tecnologías NoSQL, como MongoDB y evaluaremos sus capacidades y características de distribución. También exploramos diversas herramientas y frameworks de python que nos permitirán realizar aplicaciones para realizar la conexión y modificación de las bases de datos.

Visión general

El objetivo principal de este proyecto es desarrollar una solución efectiva para gestionar bases de datos distribuidas NoSQL, con un enfoque específico en la integración del proceso Extract, Transform, Load (ETL).
En el entorno actual, donde la cantidad y diversidad de datos continúan aumentando rápidamente, las bases de datos distribuidas NoSQL se han convertido en una opción potente para almacenar y procesar grandes volúmenes de información en entornos distribuidos. Estas bases de datos se caracterizan por su capacidad de escalar horizontalmente, su flexibilidad en la estructura de datos y su capacidad para tolerar fallos.
Sin embargo, uno de los desafíos principales en la gestión de bases de datos distribuidas NoSQL es el proceso ETL, que implica extraer datos de diversas fuentes, transformarlos según las necesidades del negocio y cargarlos en la base de datos final. La integración exitosa del ETL es esencial para asegurar la calidad y coherencia de los datos almacenados en la base de datos distribuida.
En este proyecto, llevaremos a cabo una investigación exhaustiva de las diferentes tecnologías NoSQL disponibles, como MongoDB, Cassandra o Redis, para evaluar sus características y capacidades de distribución. También exploramos diversas herramientas y frameworks de ETL, como Apache Kafka, Apache NiFi o Apache Spark, considerando su idoneidad para la integración en bases de datos distribuidas NoSQL.
La solución propuesta incluirá el diseño de una arquitectura sólida y escalable que permita la extracción eficiente de datos desde múltiples fuentes, su transformación para adaptarlos a la estructura y formato requeridos por la base de datos distribuida, y finalmente, su carga exitosa en el sistema.
Además, se abordarán aspectos clave como el rendimiento, la escalabilidad, la confiabilidad y la tolerancia a fallos de la solución propuesta. Implementaremos estrategias adecuadas de particionamiento y replicación de datos para asegurar la disponibilidad y eficiencia de la base de datos distribuida.
En resumen, este proyecto busca desarrollar una solución eficiente para la gestión de bases de datos distribuidas NoSQL, con un enfoque en la integración del proceso ETL. La solución proporcionará una infraestructura escalable y confiable para extraer, transformar y cargar datos desde múltiples fuentes hacia una base de datos distribuida, aprovechando tecnologías NoSQL y herramientas de ETL adecuadas.

Objetivos

* Diseñar una arquitectura distribuida y escalable que permita la extracción eficiente de datos desde múltiples fuentes, su transformación de acuerdo con los requisitos del negocio y su carga en la base de datos distribuida.
* Desarrollar y probar los procesos de extracción, transformación y carga (ETL) para garantizar la integridad y la consistencia de los datos en la base de datos distribuida.
  
Requerimientos

Requerimientos de hardware:
Infraestructura de servidores distribuidos que cumplan con los recursos necesarios para soportar el volumen de datos y las cargas de trabajo esperadas.
Almacenamiento suficiente para los datos, considerando la capacidad de crecimiento futuro.

Requerimientos de software:
MongoDB
Docker
Flask
Python
Plataforma de base de datos distribuida NoSQL, como MongoDB, Cassandra o Redis.
Herramientas de ETL, como Apache Kafka, Apache NiFi o Apache Spark.
Bibliotecas y frameworks adicionales necesarios para la integración y el procesamiento de datos.

Requerimientos de conectividad:
Conexión de red confiable y de alta velocidad entre los nodos de la base de datos distribuida y los sistemas de origen de datos.
Acceso a las fuentes de datos externas, como bases de datos, sistemas de archivos o servicios web, para la extracción de datos.

Requerimientos de seguridad:
Mecanismos de autenticación y autorización para garantizar el acceso seguro a los datos y la base de datos distribuida.
Encriptación de datos en tránsito y en reposo para proteger la confidencialidad y la integridad de la información.

Requerimientos de ETL:
Procesos ETL robustos y eficientes para extraer, transformar y cargar los datos en la base de datos distribuida.
Transformaciones de datos adecuadas para adaptarlos al esquema y formato de la base de datos distribuida.
Control de calidad y validación de datos durante el proceso ETL para garantizar la integridad de los datos almacenados.

Requerimientos de rendimiento y escalabilidad:
Capacidad de manejar grandes volúmenes de datos y cargas de trabajo concurrentes.
Optimización del rendimiento mediante técnicas de particionamiento y replicación de datos.
Monitoreo y ajuste continuo del rendimiento del sistema para garantizar una respuesta rápida y eficiente.

Requerimientos de tolerancia a fallos:
Implementación de mecanismos de respaldo y recuperación ante posibles fallos de hardware o software.
Manejo adecuado de errores y excepciones durante el proceso ETL para minimizar la pérdida de datos y asegurar la consistencia.

Requerimientos de documentación y capacitación:
Documentación detallada del diseño, la implementación y el funcionamiento del sistema.
Capacitación para los usuarios finales en el uso de la base de datos distribuida y las herramientas de ETL.

Documentación de Código


- ./mongors/data1:/data/db
En esta línea de código está montado el directorio ./mongors/data1 en la ruta /data/db dentro del contenedor. Esto significa que el contenido del directorio local ./mongors/data1 será accesible y utilizado por el contenedor en la ubicación /data/db.
- ./rs-init.js:/scripts/rs-init.js
En esta línea de código está montado el archivo rs-init.js desde el directorio local ./rs-init.js en la ubicación /scripts/rs-init.js dentro del contenedor.
- ./init.js:/scripts/init.js
En esta línea de código está montado el archivo init.js desde el directorio local ./init.js en la ubicación /scripts/init.js dentro del contenedor.

Pruebas
Instalamos un entorno virtual con el siguiente comando:
pip install virtualenv
virtualenv -p python3 envMongo

Red 1


Red 2






MongoDB



Desarrollo
docker-compose-replicaset.yml
version: '3.9'
services:
  mongodb-nodo1:
    container_name: mongodb-nodo1
    image: mongo
    volumes:
      - ./mongors/data1:/data/db
      - ./rs-init.js:/scripts/rs-init.js
      - ./init.js:/scripts/init.js
    networks:
      - mongors-network
    cpus: "0.5"
    mem_limit: 450m
    ports:
      - 27021:27017
    restart: always
    command: mongod --bind_ip_all --replSet "dbrs"
    depends_on:
      - mongodb-nodo3
      - mongodb-nodo2
    links:
      - mongodb-nodo3
      - mongodb-nodo2
  mongodb-nodo2:
    container_name: mongodb-nodo2
    image: mongo
    volumes:
      - ./mongors/data2:/data/db
    networks:
      - mongors-network
    cpus: "0.5"
    mem_limit: 450m
    ports:
      - 27022:27017
    restart: always
    command: mongod --bind_ip_all --replSet "dbrs"

  mongodb-nodo3:
    container_name: mongodb-nodo3
    image: mongo
    volumes:
      - ./mongors/data3:/data/db
    networks:
      - mongors-network
    cpus: "0.5"
    mem_limit: 450m
    ports:
      - 27023:27017
    restart: always
    command: mongod --bind_ip_all --replSet "dbrs"
  web:
    env_file:
      - .env
    container_name: ${WEB_HOSTETL}
    hostname: ${WEB_HOSTETL}
    build:
      context: ./app
      dockerfile: Dockerfile
    entrypoint:
      - flask
      - run
      - --host=0.0.0.0
    environment:
      FLASK_DEBUG: 1
      FLASK_APP: ./app.py
      FLASK_RUN_HOST: 0.0.0.0
      TEMPLATES_AUTO_RELOAD: 'True'
      FLASK_ENV: development
    ports: 
      - '8000:5000'
    volumes:
      - ./app:/app
    networks:
      - mongors-network
    depends_on:
      - mongodb-nodo1
      - mongodb-nodo2
      - mongodb-nodo3
networks:
  mongors-network:
    driver: bridge

docker-compose-replicaset_db2.yml
version: '3.9'
services:
  mongodb2-nodo1:
    container_name: mongodb2-nodo1
    image: mongo
    volumes:
      - ./mongors2/data1:/data/db
      - ./rs-init-bd2.js:/scripts/rs-init-bd2.js
      - ./init-bd2.js:/scripts/init-bd2.js
    networks:
      - mongors-networkbd2
    cpus: "0.5"
    mem_limit: 450m
    ports:
      - 27025:27017
    restart: always
    command: mongod --bind_ip_all --replSet "dbetl"
    depends_on:
      - mongodb2-nodo3
      - mongodb2-nodo2
    links:
      - mongodb2-nodo3
      - mongodb2-nodo2
  mongodb2-nodo2:
    container_name: mongodb2-nodo2
    image: mongo
    volumes:
      - ./mongors2/data2:/data/db
    networks:
      - mongors-networkbd2
    cpus: "0.5"
    mem_limit: 450m
    ports:
      - 27027:27017
    restart: always
    command: mongod --bind_ip_all --replSet "dbetl"
  mongodb2-nodo3:
    container_name: mongodb2-nodo3
    image: mongo
    volumes:
      - ./mongors2/data3:/data/db
    networks:
      - mongors-networkbd2
    cpus: "0.5"
    mem_limit: 450m
    ports:
      - 27026:27017
    restart: always
    command: mongod --bind_ip_all --replSet "dbetl"
  web2:
    container_name: app2
    hostname: app2
    build: 
      context: ./app2
      dockerfile: Dockerfile
    entrypoint:
      - flask
      - run
      - --host=0.0.0.0
    environment:
      FLASK_DEBUG: 1
      FLASK_APP: ./app2.py
      FLASK_RUN_HOST: 0.0.0.0
      TEMPLATES_AUTO_RELOAD: 'True'
      FLASK_ENV: development
    ports: 
      - '5000:5000'
    volumes:
      - ./app2:/app
    networks:
      - mongors-networkbd2
    depends_on:
      - mongodb2-nodo1
      - mongodb2-nodo2
      - mongodb2-nodo3
networks:
  mongors-networkbd2:
    driver: bridge

Referencias
https://www.mongodb.com/docs/manual/replication/
