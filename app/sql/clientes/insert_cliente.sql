INSERT INTO clientes (nombre_completo, contacto_1)
VALUES (%(nombre_completo)s, %(contacto_1)s)
RETURNING 
    id,
    nombre_completo,
    contacto_1,
    contacto_2,
    created_at;
