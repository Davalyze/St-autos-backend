
DROP TABLE IF EXISTS producto_imagenes CASCADE ;

CREATE TABLE producto_imagenes (
    id SERIAL PRIMARY KEY,
    vehiculo_id BIGSERIAL NOT NULL,
    img_id VARCHAR(70),
    variant_id VARCHAR(70),
    blob_name VARCHAR(255) NOT NULL,
    es_principal BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);



