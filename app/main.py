from fastapi import FastAPI
from app.api import auth, categorias, marcas, departamentos, municipios, color, combustibles, condiciones, transmisiones, clientes, vehiculos, imagenes
from fastapi.middleware.cors import CORSMiddleware
import warnings

# Ignorar todos los warnings
warnings.filterwarnings("ignore")

app = FastAPI(title="St autos Backend")

# 🟢 AGREGAR ESTO AQUÍ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Puedes restringirlo luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(categorias.router, prefix="/categorias", tags=["Categorías"])
app.include_router(marcas.router, prefix="/marcas", tags=["Marcas"])
app.include_router(departamentos.router, prefix="/departamentos", tags=["Departamentos"])
app.include_router(municipios.router, prefix="/municipios", tags=["Municipios"])
app.include_router(color.router, prefix="/colores", tags=["Colores"])
app.include_router(combustibles.router, prefix="/combustibles", tags=["Combustibles"])
app.include_router(condiciones.router, prefix="/condiciones", tags=["Condiciones"])
app.include_router(transmisiones.router, prefix="/transmisiones", tags=["Transmisiones"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(vehiculos.router, prefix="/vehiculos", tags=["Vehículos"])
app.include_router(imagenes.router, prefix="/imagenes", tags=["Imagenes"])
app.include_router(auth.router)