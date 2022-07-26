# Flask RESTful
from flask import jsonify, request
from flask_restful import Resource
# Conexion a base de datos
from utils.db_connect import get_connection
from psycopg2 import extras

class Documento(Resource):
    # Documento (datos) por Id
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

    # Eliminar por Id
    def delete(self, id_doc):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute("DELETE FROM documents WHERE id_doc = %s RETURNING *", (id_doc,))
        doc_deleted = cur.fetchone()

        conn.commit()
        conn.close()
        cur.close()

        if doc_deleted:
            return jsonify({
                "status": True,
                "msj": "Eliminado con exito!",
                "data": doc_deleted
            })
        else:
            return (
                jsonify(
                    {
                        "status": False,
                        "msj": f"Documento con id: {id_doc} no localizado - Documento no Eliminado!",
                    }
                ),
                404,
            )

    # Actualizar por Id
    def put(self, id_doc):
        
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        new_data_doc = request.get_json()

        folio_doc = new_data_doc["folio_doc"]
        tipo_doc = new_data_doc["tipo_doc"]

        cur.execute(
            "UPDATE documents SET folio_doc=%s, tipo_doc=%s WHERE id_doc=%s RETURNING *",
            (
                folio_doc,
                tipo_doc,
                id_doc,
            ),
        )
        doc_updated = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if doc_updated:
            return jsonify({
                "status": True,
                "msj": "Actualizado con exito!",
                "data": doc_updated
            })
        else:
            return (
                jsonify(
                    {
                        "status": False,
                        "msj": f"Documento con id: {id_doc} no localizado - Documento no Actualizado!",
                    }
                ),
                404,
            )

class Documentos(Resource):
    # Listado Documentos
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
    def post(self):
        # Informacion del request
        new_document = request.get_json()

        folio_doc = new_document["folio_doc"]
        tipo_doc = new_document["tipo_doc"]

        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute(
            "INSERT INTO documents (folio_doc, tipo_doc) VALUES (%s, %s) RETURNING *",
            (folio_doc,tipo_doc),
        )
        # Regresa ultimo usuario creado
        new_document_created = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if new_document_created:

            return jsonify({
                "status": True,
                "msj": "Documento creado!",
                "data": new_document_created
            })
        else:
            return jsonify({
                "status": False,
                "msj": f"Documento no creado!",
            }), 404
