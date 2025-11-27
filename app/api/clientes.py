from fastapi import APIRouter, HTTPException, Body
from app.services import clientes as svc_clientes

router = APIRouter()


@router.get("/buscar/{contacto_1}")
def buscar_cliente(contacto_1: str):
    cliente = svc_clientes.buscar_cliente_por_contacto(contacto_1)
    return {"cliente": cliente}


@router.post("/", summary="Crear un cliente nuevo")
def crear_cliente(data: dict):
    nombre = data.get("nombre_completo")
    contacto = data.get("contacto_1")

    if not nombre or not contacto:
        raise HTTPException(status_code=400, detail="nombre_completo y contacto_1 son obligatorios")

    nuevo = svc_clientes.crear_cliente(nombre, contacto)

    return {"success": True, "cliente": nuevo}

