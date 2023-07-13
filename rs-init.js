const delay = 25;

const config = {
  _id: "dbrs",
  version: 1,
  members: [
    {
      _id: 1,
      host: "mongodb-nodo1:27017",
      priority: 2
    },
    {
      _id: 2,
      host: "mongodb-nodo2:27017",
      priority: 1
    },
    {
      _id: 3,
      host: "mongodb-nodo3:27017",
      priority: 1
    }
  ]
};

rs.initiate(config, { force: true });

console.log(`****** Esperando ${delay} segundos a que se apliquen la configuración del conjunto de réplicas ******`);

setTimeout(() => {
  load("/scripts/init.js");
}, delay * 1000);
