SELECT 
    p.id,
    p.id_cliente,
    c.contacto_1 AS contacto_cliente,
    c.nombre_completo AS nombre_cliente,
    p.pedido,
    p.resuelto,
    p.created_at,
    p.updated_at
FROM pedidos p
LEFT JOIN clientes c ON c.id = p.id_cliente
ORDER BY p.created_at DESC;
