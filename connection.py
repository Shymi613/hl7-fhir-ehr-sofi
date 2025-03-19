from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(hospital, pacientes):
    uri = "mongodb+srv://laurasofia27021:Nochebuena1_@cluster0.9fw4c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[hospital]
    collection = db[pacientes]
    return collection
