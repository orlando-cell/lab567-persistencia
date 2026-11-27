# Modulo de reportes y busqueda

# ============================================================
# MODULO DE REPORTES Y BÚSQUEDAS
# Autor: Anthony Rene Terraz Terrones
# ============================================================

# ------------------------------------------------------------
# INSTRUCCIONES ANTHONY:
# Crea la función generar_reporte(lista) que recorra la lista 
# de equipos y muestre un resumen cuántos están disponibles 
# y cuántos están prestados en total.
# ------------------------------------------------------------
# 
def generar_reporte(lista_equipos):
    print("\n--- REPORTE GENERAL ---")
    total = len(lista_equipos)
    disponibles = sum(1 for eq in lista_equipos if eq["estado"] == "Disponible")
    prestados = total - disponibles
    print(f"Total equipos: {total}")
    print(f"Disponibles: {disponibles}")
    print(f"Prestados: {prestados}")