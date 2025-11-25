SELECT id, nombre
FROM marcas_vehiculo
WHERE categoria_id = %(categoria_id)s
AND activo = TRUE
ORDER BY nombre;