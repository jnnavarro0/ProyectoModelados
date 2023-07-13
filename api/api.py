from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
import threading

app = Flask(__name__)

db_hosts = [
    "mongodb2-nodo1:27017",
    "mongodb2-nodo2:27017",
    "mongodb2-nodo3:27017"
]

def connect_to_database1():
    for host in db_hosts:
        try:
            client = MongoClient(f"mongodb://{host}/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2", serverSelectionTimeoutMS=5000)
            db = client['Autos']
            collection = db['ventas']
            return collection
        except Exception as e:
            print(f"Failed to connect to {host}: {str(e)}")
    
    raise Exception("Failed to connect to all databases")

collectionData = connect_to_database1()


def connect_to_database2():
    for host in db_hosts:
        try:
            client = MongoClient(f"mongodb://{host}/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2", serverSelectionTimeoutMS=5000)
            db = client['Autos']
            collection = db['ventas']
            return collection
        except Exception as e:
            print(f"Failed to connect to {host}: {str(e)}")
    
    raise Exception("Failed to connect to all databases")

collectionEtl = connect_to_database2()

@app.route('/transfer', methods=['POST'])
def transfer_data():
    # Leer los datos de la base de datos de origen
    data = collectionData.find()
    
    # Transferir los datos a la base de datos de destino
    for document in data:
        collectionEtl.insert_one(document)
    
    return 'Transferencia de datos completada'

def watch_collection_changes():
    with collectionEtl.watch() as stream:
        for change in stream:
            print('Se ha detectado un cambio en la base de datos de origen.')
            transfer_data()

if __name__ == '__main__':
    # Iniciar un hilo para observar los cambios en la colección de origen
    change_thread = threading.Thread(target=watch_collection_changes)
    change_thread.start()
    
    # Ejecutar la aplicación Flask
    app.run()
