from app.crud import municipios as crud_municipios

def listar_municipios(departamento_id: int):
    return crud_municipios.get_municipios(departamento_id)
