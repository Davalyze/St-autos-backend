from app.db.postgres_manager import PostgresManager

def get_departamentos():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("departamentos/get_departamentos.sql")
    finally:
        pg.close()
