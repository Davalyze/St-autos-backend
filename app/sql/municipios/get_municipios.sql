SELECT id, nombre
FROM municipios
WHERE departamento_id = %(departamento_id)s
AND activo = TRUE
ORDER BY nombre;