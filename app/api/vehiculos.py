from fastapi import APIRouter, HTTPException
from app.services import vehiculos as svc_vehiculos

router = APIRouter()

@router.post("/", summary="Crear un vehículo desde captación")
def crear_vehiculo(data: dict):

    obligatorio = [
        "vehiculo", "categoria_id", "marca_id", "anio",
        "condicion_id", "precio_base", "combustible_id",
        "color_id", "transmision_id",
        "ubi_departamento_id", "ubi_municipio_id",
        "id_propietario"
    ]

    for campo in obligatorio:
        if campo not in data or data[campo] in [None, ""]:
            raise HTTPException(400, f"El campo '{campo}' es obligatorio")

    nuevo = svc_vehiculos.crear_vehiculo(data)

    if not nuevo:
        raise HTTPException(500, "Error creando el vehículo")

    return {"success": True, "vehiculo": nuevo}


@router.get("/", summary="Obtener todos los vehículos")
def obtener_vehiculos():

    vehiculos = svc_vehiculos.obtener_vehiculos()

    return {"vehiculos": vehiculos}

@router.get("/{id}", summary="Obtener detalle de un vehículo por ID")
def obtener_vehiculo(id: int):
    vehiculo = svc_vehiculos.obtener_vehiculo_por_id(id)

    if not vehiculo:
        raise HTTPException(404, "Vehículo no encontrado")

    return {"vehiculo": vehiculo}
