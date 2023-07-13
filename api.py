from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure
import time

db_hosts1 = [
        "mongodb://127.0.0.1:27021/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2",
        "mongodb://127.0.0.1:27022/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2",
        "mongodb://127.0.0.1:27023/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2"
    ]

db_hosts2 = [
        "mongodb://127.0.0.1:27025/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2",
        "mongodb://127.0.0.1:27026/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2",
        "mongodb://127.0.0.1:27027/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2"
    ]
    

def connect_to_database(db_hosts):
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

collection1 = connect_to_database(db_hosts1)
collection2 = connect_to_database(db_hosts2)


from datetime import datetime

def verify_and_update(document):
    # Verificar campos vacíos
    if any(value == "" or value is None for value in document.values()):
        return "Documento descartado. Posee campos vacíos."


    # Actualizar datos por año del automóvil
    document['Car Year'] = int(document['Car Year'])

    # Verificar año coherente
    current_year = datetime.now().year
    car_year = document['Car Year']
    if car_year < 1900 or car_year > current_year:
        return "Documento descartado. Año de automóvil incoherente."

    # Verificar y actualizar en la colección2
    query = {"id": document["id"]}
    existing_document = collection2.find_one(query)

    if not existing_document:
        collection2.insert_one(document)
        return "Documento insertado en la colección2."
    else:
        is_equal = True
        for field in document:
            if field != "_id" and document[field] != existing_document[field]:
                is_equal = False
                break

        if is_equal:
            return "El documento es igual al existente en la colección2. Se descarta."
        else:
            collection2.update_one(query, {"$set": document})
            return "Documento actualizado en la colección2."


def extract_transform(collection):
    # Extraer los datos de la colección1
    data = list(collection.find())

    # Verificar campos vacíos y cambiar formato de fecha
    transformed_data = []
    for document in data:
        if all(value != "" and value is not None for value in document.values()):
            if 'Date' in document:
                date_str = document['Date']
                try:
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                    document['Year'] = date_obj.year
                    document['Month'] = date_obj.month
                    document['Day'] = date_obj.day
                except ValueError:
                    continue
            transformed_data.append(document)

    # Ordenar los datos por año del automóvil
    transformed_data.sort(key=lambda x: x['Car Year'])

    return transformed_data


document = {
    'id': 1,
    'Date': '2023-08-01',
    'Salesperson': 'John Doe',
    'Customer Name': 'Alice',
    'Car Make': 'Toyota',
    'Car Model': 'Corolla',
    'Car Year': 2025,
    'Sale Price': 25000,
    'Commission Rate': 0.05,
    'Commission Earned': 1251
}

verify_and_update(document)