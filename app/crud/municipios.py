from app.db.postgres_manager import PostgresManager

def get_municipios(departamento_id: int):
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file(
            "municipios/get_municipios.sql",
            params={"departamento_id": departamento_id}
        )
    finally:
        pg.close()
