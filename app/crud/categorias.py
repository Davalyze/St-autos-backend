from app.db.postgres_manager import PostgresManager

pg = PostgresManager()

def get_categorias():
    """
    Ejecuta la mconsulta de Categorías (Carros y camionetas, Motos).
    Retorna:
        list[dict]: Lista de Categorías.
    """
    
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("categorias/get_categorias.sql")
    finally:
        pg.close()