from app.db.postgres_manager import PostgresManager


# -------------------------------------------------------
# 📋 1. Obtener pedidos
# -------------------------------------------------------
def obtener_pedidos():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("pedidos/get_pedidos.sql")
    finally:
        pg.close()


# -------------------------------------------------------
# 🆕 2. Crear pedido
# -------------------------------------------------------
def crear_pedido(id_cliente: int, pedido: str):
    pg = PostgresManager()
    try:
        return pg.execute_insert_returning_from_file(
            "pedidos/insert_pedido.sql",
            {
                "id_cliente": id_cliente,
                "pedido": pedido
            }
        )
    finally:
        pg.close()


# -------------------------------------------------------
# 🔄 3. Actualizar estado del pedido (pendiente → resuelto)
# -------------------------------------------------------
def actualizar_estado(id: int, resuelto: bool):
    pg = PostgresManager()
    try:
        return pg.execute_insert_returning_from_file(
            "pedidos/update_estado_pedido.sql",
            {
                "id": id,
                "resuelto": resuelto
            }
        )
    finally:
        pg.close()
