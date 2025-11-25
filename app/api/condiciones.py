from fastapi import APIRouter
from app.services import condiciones as svc_cond

router = APIRouter()

@router.get("/", summary="Lista condiciones del vehículo")
def listar_condiciones():
    return {"condiciones": svc_cond.listar_condiciones()}