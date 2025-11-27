from app.db.postgres_manager import PostgresManager

def crear_vehiculo(data: dict):
    pg = PostgresManager()
    try:
        return pg.execute_insert_returning_from_file(
            "vehiculos/insert_vehiculo.sql",
            data
        )
    finally:
        pg.close()

def obtener_vehiculos():
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file("vehiculos/get_vehiculos.sql")
    finally:
        pg.close()


def obtener_vehiculo_por_id(id: int):
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file(
            "vehiculos/get_vehiculo_por_id.sql",
            {"id": id}
        )
    finally:
        pg.close()
