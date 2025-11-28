CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
    pedido TEXT NOT NULL,
    resuelto BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
