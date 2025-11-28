INSERT INTO producto_imagenes (vehiculo_id, blob_name, es_principal)
VALUES (%(vehiculo_id)s, %(blob_name)s, %(es_principal)s)
RETURNING id;