from fastapi import APIRouter
from app.services import color as svc_color

router = APIRouter()

@router.get("/", summary="Lista los colores")
def listar_colores():
    return {"colores": svc_color.listar_colores()}
