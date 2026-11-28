# Modulo de utilidades y validaciones

# ============================================================
# MODULO DE UTILIDADES Y VALIDACIONES
# Autor: Cristian Omar Huamán Rojas
# ============================================================

def validar_texto(valor):
    if valor is None or valor.strip() == "":
        print("Error: El campo no puede estar vacio.")
        return False
    return True


