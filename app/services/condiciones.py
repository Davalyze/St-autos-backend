from app.crud import condiciones as crud_cond

def listar_condiciones():
    return crud_cond.get_condiciones()
