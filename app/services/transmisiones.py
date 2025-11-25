from app.crud import transmisiones as crud_trans

def listar_transmisiones():
    return crud_trans.get_transmisiones()