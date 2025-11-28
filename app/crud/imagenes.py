from app.db.postgres_manager import PostgresManager


# -------------------------------------------------------
# 📤 1. Insertar una imagen de un vehículo
# -------------------------------------------------------
def crear_imagen(vehiculo_id: int, blob_name: str, es_principal: bool):
    pg = PostgresManager()
    try:
        return pg.execute_non_query_from_file(
            "imagenes/insert_imagenes.sql",
            {
                "vehiculo_id": vehiculo_id,
                "blob_name": blob_name,
                "es_principal": es_principal
            }
        )
    finally:
        pg.close()


# -------------------------------------------------------
# 📸 2. Obtener TODAS las imágenes del vehículo
# -------------------------------------------------------
def obtener_imagenes(vehiculo_id: int):
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file(
            "imagenes/get_imagenes.sql",
            {"vehiculo_id": vehiculo_id}
        )
    finally:
        pg.close()


# -------------------------------------------------------
# ⭐ 3. Obtener la imagen principal del vehículo
# -------------------------------------------------------
def obtener_imagen_principal(vehiculo_id: int):
    pg = PostgresManager()
    try:
        return pg.execute_query_from_file(
            "imagenes/get_imagen_principal.sql",
            {"vehiculo_id": vehiculo_id}
        )
    finally:
        pg.close()
