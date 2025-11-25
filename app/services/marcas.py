from app.crud import marcas as crud_marcas

def listar_marcas(categoria_id: int):
    """
    Lógica de negocio para listar marcas filtradas por categoría.
    """
    return crud_marcas.get_marcas(categoria_id)
