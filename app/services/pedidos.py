from app.crud import pedidos as crud_pedidos


# -------------------------------------------------------
# 🆕 Crear pedido
# -------------------------------------------------------
def crear_pedido(id_cliente: int, pedido: str):
    row = crud_pedidos.crear_pedido(id_cliente, pedido)

    if not row:
        return None

    return row


# -------------------------------------------------------
# 📋 Listar pedidos
# -------------------------------------------------------
def obtener_pedidos():
    rows = crud_pedidos.obtener_pedidos()

    if not rows:
        return []

    return rows


# -------------------------------------------------------
# 🔄 Cambiar estado (pendiente → resuelto)
# -------------------------------------------------------
def actualizar_estado(id: int, resuelto: bool):
    row = crud_pedidos.actualizar_estado(id, resuelto)

    return row
