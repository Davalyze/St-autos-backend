SELECT id, vehiculo_id, blob_name, es_principal, created_at
FROM producto_imagenes
WHERE vehiculo_id = %(vehiculo_id)s
AND es_principal = TRUE
ORDER BY id ASC
LIMIT 1;