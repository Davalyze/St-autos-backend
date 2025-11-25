from fastapi import APIRouter
from app.services import marcas as svc_marcas

router = APIRouter()

@router.get("/{categoria_id}", summary="Lista las marcas por categoría")
def listar_marcas(categoria_id: int):
    """
    Endpoint para obtener las marcas de una categoría.
    """
    return {
        "marcas": svc_marcas.listar_marcas(categoria_id)
    }
