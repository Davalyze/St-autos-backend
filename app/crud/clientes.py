from app.db.postgres_manager import PostgresManager

# -------------------------------------------------------
# 🔍 Buscar cliente por contacto_1
# -------------------------------------------------------
def get_cliente_por_contacto(contacto_1: str):
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file(
            "clientes/get_cliente_por_contacto.sql",
            {"contacto_1": contacto_1}
        )
    finally:
        pg.close()


# -------------------------------------------------------
# 🆕 Crear cliente
# -------------------------------------------------------
def crear_cliente(nombre_completo: str, contacto_1: str):
    pg = PostgresManager()
    try:
        return pg.execute_insert_returning_from_file(
            "clientes/insert_cliente.sql",
            {
                "nombre_completo": nombre_completo,
                "contacto_1": contacto_1
            }
        )
    finally:
        pg.close()
