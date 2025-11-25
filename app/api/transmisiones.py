from fastapi import APIRouter
from app.services import transmisiones as svc_trans

router = APIRouter()

@router.get("/", summary="Lista transmisiones del vehículo")
def listar_transmisiones():
    return {"transmisiones": svc_trans.listar_transmisiones()}