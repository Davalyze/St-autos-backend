from fastapi import APIRouter
from app.services import municipios as svc_municipios

router = APIRouter()

@router.get("/{departamento_id}", summary="Lista municipios por departamento")
def listar_municipios(departamento_id: int):
    return {"municipios": svc_municipios.listar_municipios(departamento_id)}