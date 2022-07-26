# Flask RESTful
from flask import jsonify
from flask_restful import Resource
# Conexion a base de datos
from utils.db_connect import get_connection
from psycopg2 import extras

class Documento(Resource):
    def get(self, id_doc):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute("SELECT * FROM documents WHERE id_doc = %s", (id_doc,))
        document_by_id = cur.fetchone()

        if document_by_id:

            return jsonify({
                "status": True,
                "msj": "Documento localizado!",
                "data": document_by_id
            })
        else:
            return jsonify({
                "status": False,
                "msj": f"Documento con id: {id_doc} no localizado - Documento no disponible!",
            }), 404


    def delete(self, id_doc):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, id_doc):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class DocumentosLista(Resource):
    def get(self):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute("SELECT * FROM documents")
        documentos = cur.fetchall()

        cur.close()
        conn.close()

        if documentos:
            return jsonify({
                "status": True,
                "msj": "Listado documentos",
                "data": documentos
            })
        else:
            return (
                jsonify(
                    {
                        "status": False,
                        "msj": f"Documentos no localizados - Lista documentos no disponible!",
                    }
                ),
                404,
            )
