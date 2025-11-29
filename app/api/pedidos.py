from fastapi import APIRouter, HTTPException
from app.services import pedidos as svc_pedidos

router = APIRouter()


# -------------------------------------------------------
# 🆕 Crear pedido
# -------------------------------------------------------
@router.post("/", summary="Crear un pedido")
def crear_pedido(data: dict):
    id_cliente = data.get("id_cliente")
    pedido = data.get("pedido")

    if not id_cliente or not pedido:
        raise HTTPException(status_code=400, detail="id_cliente y pedido son obligatorios")

    nuevo = svc_pedidos.crear_pedido(id_cliente, pedido)
    return {"success": True, "pedido": nuevo}


# -------------------------------------------------------
# 📋 Listar pedidos
# -------------------------------------------------------
@router.get("/", summary="Listar pedidos")
def listar_pedidos():
    pedidos = svc_pedidos.obtener_pedidos()
    return {"pedidos": pedidos}


# -------------------------------------------------------
# 🔄 Cambiar estado
# -------------------------------------------------------
@router.put("/{id}/estado", summary="Actualizar estado del pedido")
def actualizar_estado(id: int, data: dict):
    resuelto = data.get("resuelto")

    if resuelto is None:
        raise HTTPException(status_code=400, detail="resuelto es obligatorio")

    actualizado = svc_pedidos.actualizar_estado(id, resuelto)

    return {"success": True, "pedido": actualizado}
