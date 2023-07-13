from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure
import time
import secrets


app = Flask(__name__)

def initiate_replica_set():
    try:
        client = MongoClient("mongodb2-nodo1:27017")
        admin_db = client.admin
        admin_db.command("replSetInitiate")
        print("Replica set initiated successfully.")
    except Exception as e:
        print(f"Failed to initiate replica set: {str(e)}")

initiate_replica_set()

def connect_to_database():
    db_hosts = [
        "mongodb2-nodo1:27017",
        "mongodb2-nodo2:27017",
        "mongodb2-nodo3:27017"
    ]
    
    connected = False
    while not connected:
        for host in db_hosts:
            try:
                client = MongoClient(host, serverSelectionTimeoutMS=2000)
                client.server_info()  
                db = client['Autos']
                collection = db['ventas']
                return collection
            except ConnectionFailure as e:
                print(f"Failed to connect to {host}: {str(e)}")
        

        print("Failed to connect to all databases. Retrying...")
        time.sleep(5)  

collection = connect_to_database()


@app.route('/')
def index():
    if collection is None:
        return "Failed to connect to any database"
    data = collection.find()
    try:
        return render_template('index.html', data=data, item={})
    except Exception as e:
        return str(e)
    



if __name__ == '__main__':
    app.run()
