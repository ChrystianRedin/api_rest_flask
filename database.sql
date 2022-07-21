-- TABLA USUARIOS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users (
    id_user uuid DEFAULT uuid_generate_v4 (),
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
