from flask import Flask
# Importacion de Rutas 
from routes.users import users_routes

app = Flask(__name__)

# Registro de la ruta
app.register_blueprint(users_routes)