from app.crud import vehiculos as crud_vehiculos
from app.services import a_transformer as transformer 
from app.db.azure_connection import AzureBlobService
azure = AzureBlobService()
def crear_vehiculo(data: dict):
    """
    Crea un vehículo completo desde captación.
    """
    row = crud_vehiculos.crear_vehiculo(data)

    if not row:
        return None

    return row

def obtener_vehiculos():
    """
    Obtiene todos los vehículos completos para el catálogo.
    """
    rows = crud_vehiculos.obtener_vehiculos()
    df_vehiculos = transformer.sql_to_df(rows)
    if 'blob_name' in df_vehiculos.columns:
        df_vehiculos['imagen_url'] = df_vehiculos['blob_name'].apply(
            lambda x: azure.build_blob_url(x) if x else None
        )
    else:
        df_vehiculos['imagen_url'] = None
    print(df_vehiculos)
    rows = transformer.df_to_dict(df_vehiculos)

    return rows

def obtener_vehiculo_por_id(id: int):
    row = crud_vehiculos.obtener_vehiculo_por_id(id)

    if not row:
        return None

    # row viene como lista de dicts porque usamos execute_query
    return row[0]
