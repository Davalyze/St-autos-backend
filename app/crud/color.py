from app.db.postgres_manager import PostgresManager

def get_colores():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("color/get_color.sql")
    finally:
        pg.close()
