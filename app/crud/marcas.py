from app.db.postgres_manager import PostgresManager

pg = PostgresManager()

def get_marcas(categoria_id: int):
    """
    Ejecuta la consulta de Marcas según la categoría.
    """
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file(
            "marcas/get_marcas.sql",
            params={"categoria_id": categoria_id}
        )
    finally:
        pg.close()
