from app.db.postgres_manager import PostgresManager

def get_combustibles():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("combustibles/get_combustibles.sql")
    finally:
        pg.close()
