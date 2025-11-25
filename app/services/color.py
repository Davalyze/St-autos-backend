from app.crud import color as crud_color

def listar_colores():
    return crud_color.get_colores()
