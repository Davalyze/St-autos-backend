from app.db.postgres_manager import PostgresManager

def get_transmisiones():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("transmisiones/get_transmisiones.sql")
    finally:
        pg.close()
