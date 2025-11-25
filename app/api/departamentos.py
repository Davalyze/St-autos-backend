from fastapi import APIRouter
from app.services import departamentos as svc_deptos

router = APIRouter()

@router.get("/", summary="Lista los departamentos")
def listar_departamentos():
    return {"departamentos": svc_deptos.listar_departamentos()}