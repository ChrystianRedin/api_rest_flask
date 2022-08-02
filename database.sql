-- TABLA USUARIOS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users (
    id_user uuid DEFAULT uuid_generate_v4(),
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE documents (
    id_doc uuid DEFAULT uuid_generate_v4(),
    folio_doc VARCHAR(255),
    tipo_doc VARCHAR(255),
    fecha_doc VARCHAR(255),
    asunto_doc VARCHAR(255),
    depto_asignar VARCHAR(255),
    titular_asignar VARCHAR(255),
    contenido_doc VARCHAR(255),
    copia_doc VARCHAR(255),
    slbr_doc VARCHAR(255),
    id_firma VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
