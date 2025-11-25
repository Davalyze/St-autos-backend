from app.crud import departamentos as crud_deptos

def listar_departamentos():
    return crud_deptos.get_departamentos()
