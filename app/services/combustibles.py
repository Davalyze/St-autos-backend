from app.crud import combustibles as crud_combustibles

def listar_combustibles():
    return crud_combustibles.get_combustibles()
