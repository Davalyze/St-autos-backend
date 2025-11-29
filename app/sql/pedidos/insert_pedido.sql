INSERT INTO pedidos (id_cliente, pedido)
VALUES (%(id_cliente)s, %(pedido)s)
RETURNING *;