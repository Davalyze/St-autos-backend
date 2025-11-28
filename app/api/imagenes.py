from fastapi import APIRouter, HTTPException
from app.services import imagenes as svc_imagenes
from app.db.azure_connection import AzureBlobService
import base64

router = APIRouter()
azure = AzureBlobService()


@router.post("/{vehiculo_id}/imagenes")
def subir_imagen(vehiculo_id: int, data: dict):

    filename = data.get("filename")       # <-- AHORA COINCIDE CON EL FRONT
    file_base64 = data.get("file_base64") # <-- Lo que envía el frontend
    es_principal = data.get("es_principal", False)

    if not filename:
        raise HTTPException(status_code=400, detail="filename es obligatorio")

    if not file_base64:
        raise HTTPException(status_code=400, detail="file_base64 es obligatorio")

    # ==========================================
    # 1️⃣ Subir a Azure Blob desde Base64
    # ==========================================
    try:
        blob_service = azure.connect()
        container = blob_service.get_container_client(azure.container)
        blob_client = container.get_blob_client(filename)

        img_bytes = base64.b64decode(file_base64)

        blob_client.upload_blob(img_bytes, overwrite=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error subiendo a Azure: {e}")

    # ==========================================
    # 2️⃣ Registrar en PostgreSQL
    # ==========================================
    nueva = svc_imagenes.registrar_imagen(
        vehiculo_id=vehiculo_id,
        blob_name=filename,
        es_principal=es_principal
    )

    return {"success": True, "imagen": nueva}
