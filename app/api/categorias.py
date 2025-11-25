from fastapi import APIRouter, Query
from typing import Optional
from app.services import categorias as svc_categorias

router = APIRouter()

@router.get("/", summary="Lista las categorías ")
def listar_categorias(
):
    """
    Endpoint para obtener la lista de categorías.
    Returns:
        dict: Diccionario con la lista de categorías.
    """
    return {"categorias": svc_categorias.listar_categorias()}