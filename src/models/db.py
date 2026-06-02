from pymongo import MongoClient
from os import environ

# Conecta no Mongo, pela variavel ambiente definida no docker-compose
client = MongoClient(environ.get("MONGO_URL"))

# Cria um banco de dados chamado db_chat
db = client.db_chat