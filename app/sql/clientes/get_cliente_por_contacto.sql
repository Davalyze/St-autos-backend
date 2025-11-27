SELECT 
    id,
    nombre_completo,
    contacto_1,
    contacto_2,
    created_at
FROM clientes
WHERE contacto_1 = %(contacto_1)s;
