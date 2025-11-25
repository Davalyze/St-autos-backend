from app.db.postgres_manager import PostgresManager

def get_condiciones():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("condiciones/get_condiciones.sql")
    finally:
        pg.close()
