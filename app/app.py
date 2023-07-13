from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure
import time
import secrets
import subprocess

app = Flask(__name__)

def initiate_replica_set():
    try:
        client = MongoClient("mongodb-nodo1:27017")
        admin_db = client.admin
        admin_db.command("replSetInitiate")
        print("Replica set initiated successfully.")
    except Exception as e:
        print(f"Failed to initiate replica set: {str(e)}")

initiate_replica_set()

def connect_to_database():
    db_hosts = [
        "mongodb-nodo1:27017",
        "mongodb-nodo2:27017",
        "mongodb-nodo3:27017"
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
    
    
@app.route('/delete', methods=['POST'])
def delete_data():
    selected_ids = request.form.getlist('options[]')
    try:
        object_ids = [ObjectId(id) for id in selected_ids]
        result = collection.delete_many({'_id': {'$in': object_ids}})
        return redirect('/')
    except Exception as e:
        return str(e)

id_length = 5
new_id = secrets.token_hex(id_length)[:id_length].upper()

@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        id = new_id
        date = request.form.get('date')
        salesperson = request.form.get('salesperson')
        customer_name = request.form.get('customer_name')
        car_make = request.form.get('car_make')
        car_model = request.form.get('car_model')
        car_year = request.form.get('car_year')
        sale_price = request.form.get('sale_price')
        commission_rate = request.form.get('commission_rate')
        commission_earned = request.form.get('commission_earned')
        
        new_document = {
            'id': id,
            'Date': date,
            'Salesperson': salesperson,
            'Customer Name': customer_name,
            'Car Make': car_make,
            'Car Model': car_model,
            'Car Year': car_year,
            'Sale Price': sale_price,
            'Commission Rate': commission_rate,
            'Commission Earned': commission_earned
        }
        
        result = collection.insert_one(new_document)
        return redirect('/')
    
    except Exception as e:
        return str(e)
    
    
    
@app.route('/update', methods=['POST'])
def update_data():
    try:
        id = request.form.get('id')  # Obtén el ID del registro que se está actualizando
        salesperson = request.form.get('salesperson')
        customer_name = request.form.get('customer')
        car_make = request.form.get('make')
        car_model = request.form.get('model')
        car_year = request.form.get('year')
        sale_price = request.form.get('price')
        commission_rate = request.form.get('rate')
        commission_earned = request.form.get('earned')
        
        filter = {'_id': ObjectId(id)}

        # Definir los cambios a realizar en el documento
        update = {'$set': {
                'Salesperson': salesperson,
                'Customer Name': customer_name,
                'Car Make': car_make,
                'Car Model': car_model,
                'Car Year': car_year,
                'Sale Price': sale_price,
                'Commission Rate': commission_rate,
                'Commission Earned': commission_earned
            }}

        # Actualizar el documento
        result = collection.update_one(filter, update)
        
        
        return redirect('/')
    
    except Exception as e:
        return str(e)
    
    
@app.route('/run_script', methods=['POST'])
def run_script():
    subprocess.run(['python', '../api.py'])
    return 'Script ejecutado'



if __name__ == '__main__':
    app.run()
