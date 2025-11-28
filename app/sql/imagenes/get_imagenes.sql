SELECT id, vehiculo_id, blob_name, es_principal, created_at
FROM producto_imagenes
WHERE vehiculo_id = %(vehiculo_id)s
ORDER BY id ASC;