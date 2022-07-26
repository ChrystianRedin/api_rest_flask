# Conexion a base de datos
from utils.db_connect import get_connection
# Importaciones
from flask import Blueprint, request, jsonify
from psycopg2 import extras

# exportar rutas de documentos a app.py
documentos_routes = Blueprint('documentos_routes',__name__)

# Crear Documento
@documentos_routes.post("/api/documents")
def create_documentos():
    # Informacion del request
    new_document = request.get_json()

    folio = new_document["folio"]
    tipo_doc = new_document["tipo_doc"]

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute(
        "INSERT INTO documents (folio_doc, tip_doc) VALUES (%s, %s) RETURNING *",
        (folio,tipo_doc),
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

# Documento por ID
@documentos_routes.get("/api/documents/<id_doc>")
def get_document_id(id_doc):

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

# Listado Documentos
@documentos_routes.get("/api/documents")
def get_docs():
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


# Actualizar Documento
@documentos_routes.put("/api/documents/<id_doc>")
def update_doc(id_doc):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_data_doc = request.get_json()

    folio = new_data_doc["folio"]
    tipo_doc = new_data_doc["tipo_doc"]

    cur.execute(
        "UPDATE documents SET folio_doc=%s, tip_doc=%s WHERE id_doc=%s RETURNING *",
        (
            folio,
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

# Eliminar Usuario
@documentos_routes.delete("/api/documents/<id_doc>")
def delete_docs(id_doc):
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
