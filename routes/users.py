# Conexion a base de datos
from utils.db_connect import get_connection
# Importaciones
from flask import Blueprint, request, jsonify
from psycopg2 import extras
from cryptography.fernet import Fernet

# exportar rutas de usuarios a app.py
users_routes = Blueprint('users_routes',__name__)

# Funcion para encriptar password
key = Fernet.generate_key()

# Crear Usuario
@users_routes.post("/api/users")
def create_users():
    # Informacion del request
    new_user = request.get_json()
    username = new_user["username"]
    email = new_user["email"]
    password = Fernet(key).encrypt(bytes(new_user["password"], "utf-8"))

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING *",
        (username, email, password),
    )
    # Regresa ultimo usuario creado
    new_created_user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if new_created_user:

        return jsonify({
            "status": True,
            "msj": "Usuario creado!",
            "data": new_created_user
        })
    else:
        return jsonify({
            "status": False,
            "msj": f"Usuario no creado!",
        }), 404

# Usuario por Id
@users_routes.get("/api/users/<id_user>")
def get_user_id(id_user):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM users WHERE id_user = %s", (id_user,))
    user_by_id = cur.fetchone()

    if user_by_id:

        return jsonify({
            "status": True,
            "msj": "Usuario localizado!",
            "data": user_by_id
        })
    else:
        return jsonify({
            "status": False,
            "msj": f"Usuario con id: {id_user} no localizado - Usuario no disponible!",
        }), 404

# Listado Usuarios
@users_routes.get("/api/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    cur.close()
    conn.close()

    if users:
        return jsonify({
            "status": True,
            "msj": "Listado usuarios",
            "data": users
        })
    else:
        return (
            jsonify(
                {
                    "status": False,
                    "msj": f"Usuarios no localizados - Lista usuario no disponible!",
                }
            ),
            404,
        )

# Actualizar Usuario
@users_routes.put("/api/users/<id_user>")
def update_user(id_user):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_data_user = request.get_json()

    username = new_data_user["username"]
    email = new_data_user["email"]
    password = Fernet(key).encrypt(bytes(new_data_user["password"], "utf-8"))

    cur.execute(
        "UPDATE users SET username=%s, password=%s, email=%s WHERE id_user=%s RETURNING *",
        (
            username,
            password,
            email,
            id_user,
        ),
    )
    user_updated = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if user_updated:
        return jsonify({
            "status": True,
            "msj": "Actualizado con exito!",
            "data": user_updated
        })
    else:
        return (
            jsonify(
                {
                    "status": False,
                    "msj": f"Usuario con id: {id_user} no localizado - Usuario no Actualizado!",
                }
            ),
            404,
        )

# Eliminar Usuario
@users_routes.delete("/api/users/<id_user>")
def delete_user(id_user):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("DELETE FROM users WHERE id_user = %s RETURNING *", (id_user,))
    user_deleted = cur.fetchone()

    conn.commit()

    conn.close()
    cur.close()

    if user_deleted:
        return jsonify({
            "status": True,
            "msj": "Eliminado con exito!",
            "data": user_deleted
        })
    else:
        return (
            jsonify(
                {
                    "status": False,
                    "msj": f"Usuario con id: {id_user} no localizado - Usuario no Eliminado!",
                }
            ),
            404,
        )
