-- Extension UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- TABLA Users
CREATE TABLE users (
    id_user uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    activo BOOLEAN,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- FIN TABLA Users

-- TABLA Documents
CREATE TABLE documents (
    id_doc uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    id_user uuid,
    folio_doc VARCHAR(255),
    tipo_doc VARCHAR(255),
    fecha_doc DATE,
    asunto_doc VARCHAR(255),
    depto_asignar VARCHAR(255),
    titular_asignar VARCHAR(255),
    contenido_doc TEXT,
    copia_doc VARCHAR(255),
    slbr_doc VARCHAR(255),
    cancelado BOOLEAN,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
    ALTER TABLE documents ADD CONSTRAINT fk_document_user FOREIGN KEY (id_user) REFERENCES users(id_user);
-- FIN TABLA Documents

-- TABLA FIRMANTES (Firma Electronica)
CREATE TABLE firmantes_docs (
    id_firma uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    id_doc uuid,
    id_user uuid,
    response TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
    ALTER TABLE firmantes_docs ADD CONSTRAINT fk_firma_document FOREIGN KEY (id_doc) REFERENCES documents(id_doc) ON DELETE CASCADE;
    ALTER TABLE firmantes_docs ADD CONSTRAINT fk_firma_user FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE SET NULL;
-- FIN TABLA Firmantes_Docs

-- TABLA usuario_sistemas (Usuario Sistemas)
CREATE TABLE usuario_sistemas (
    id_user_sys uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    id_user uuid,
    nombre_sistema VARCHAR(255),
    id_sistema uuid,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
    ALTER TABLE usuario_sistemas ADD CONSTRAINT fk_usersys_userdocs FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE SET NULL;
-- FIN TABLA Firmantes_Docs