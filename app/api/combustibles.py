from fastapi import APIRouter
from app.services import combustibles as svc_comb

router = APIRouter()

@router.get("/", summary="Lista los combustibles")
def listar_combustibles():
    return {"combustibles": svc_comb.listar_combustibles()}