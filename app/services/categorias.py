from app.crud import categorias as crud_categorias
from app.services import a_transformer as transformer 


def listar_categorias():
    """
    Lógica de negocio para listar categorías.
    """
    rows = crud_categorias.get_categorias()
    return rows