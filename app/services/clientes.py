from app.crud import clientes as crud_clientes


# -------------------------------------------------------
# 🔍 1. Buscar cliente por contacto_1
# -------------------------------------------------------
def buscar_cliente_por_contacto(contacto_1: str):
    """
    Busca un cliente por su número de contacto_1.
    Retorna un dict o None.
    """
    rows = crud_clientes.get_cliente_por_contacto(contacto_1)

    # rows puede ser [] o [dict]
    if not rows:
        return None

    return rows[0]  # primer registro


# -------------------------------------------------------
# 🆕 2. Crear cliente
# -------------------------------------------------------
# -------------------------------------------------------
# 🆕 2. Crear cliente
# -------------------------------------------------------
def crear_cliente(nombre_completo: str, contacto_1: str):
    cliente = crud_clientes.crear_cliente(nombre_completo, contacto_1)

    if not cliente:
        return None

    return cliente 

