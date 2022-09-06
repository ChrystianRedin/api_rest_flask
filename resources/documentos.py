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

        cur.execute("""
            SELECT * FROM documents
            WHERE id_doc = %s""", 
            (id_doc,))
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

        form = request.get_json()
        folio_doc = form.get("folio_doc")
        tipo_doc = form.get("tipo_doc")
        fecha_doc = form.get("fecha_doc") 
        asunto_doc = form.get("asunto_doc")
        depto_asignar = form.get("depto_asignar")
        titular_asignar= form.get("titular_asignar")
        contenido_doc = form.get("contenido_doc")
        copia_doc = form.get("copia_doc")
        slbr_doc = form.get("slbr_doc")
        id_user= form.get("id_user")
        
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute(
            """ UPDATE documents SET 
            folio_doc=%s, 
            tipo_doc=%s,
            fecha_doc=%s,
            asunto_doc=%s,
            depto_asignar=%s,
            titular_asignar=%s,
            contenido_doc=%s,
            copia_doc=%s,
            slbr_doc=%s
            WHERE id_doc=%s 
            RETURNING * """,
            (
                folio_doc,
                tipo_doc,
                fecha_doc,
                asunto_doc,
                depto_asignar,
                titular_asignar,
                contenido_doc,
                copia_doc,
                slbr_doc,
                id_doc
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

    # Creacion del Documento
    def post(self):
        # Informacion del request
        form = request.get_json()

        folio_doc = form.get("folio_doc")
        tipo_doc = form.get("tipo_doc")
        fecha_doc = form.get("fecha_doc") 
        asunto_doc = form.get("asunto_doc")
        depto_asignar = form.get("depto_asignar")
        titular_asignar= form.get("titular_asignar")
        contenido_doc = form.get("contenido_doc")
        copia_doc = form.get("copia_doc")
        slbr_doc = form.get("slbr_doc")
        id_user = form.get("id_user")

        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        # Insert en Tabla documents
        cur.execute(
            "INSERT INTO documents (folio_doc, tipo_doc, fecha_doc, asunto_doc, depto_asignar, contenido_doc, copia_doc, slbr_doc, id_user) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *",
            (   
                folio_doc,
                tipo_doc,
                fecha_doc,
                asunto_doc,
                depto_asignar,
                contenido_doc,
                copia_doc,
                slbr_doc,
                id_user
            ),
        )
        # Regresa ultimo usuario creado
        new_document_created = cur.fetchone()
        conn.commit()
        #cur.close()

        # Si el documento se Creó 
        if new_document_created:

            # ID del Documento que se acaba de crear
            id_documento_creado = new_document_created["id_doc"]

            # Insertar Titulares Que Firmaran Documento a la Tabla  (firmantes_docs)
            # For de Titulares
            for titular in titular_asignar:

                # UUID del Titular
                id_titular = titular["id_user"]

                # Insert Tabla Firmantes (Firma electronica)
                cur.execute(
                    "INSERT INTO firmantes_docs (id_doc, id_user) VALUES (%s,%s) RETURNING *",
                    (   
                        id_documento_creado,
                        id_titular 
                    ),
                )
                #new_titular_insert += cur.fetchone()
                conn.commit()

            
            # Cerrar Conexion Base de Datos
            cur.close()
            conn.close()

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


class Documento_Id_User(Resource):
    # Documentos Por Id Usuario
    def get(self, id_user):
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)

        cur.execute("""
            SELECT * FROM documents
            WHERE id_user = %s""", 
            (id_user,))
        documentos = cur.fetchall()

        cur.close()
        conn.close()

        if documentos:
            return jsonify({
                "status": True,
                "msj": "Listado documentos por ID usuario",
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