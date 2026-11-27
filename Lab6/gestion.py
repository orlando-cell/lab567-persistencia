# Modulo de gestion de equipos

# ============================================================
# MODULO DE GESTIÓN DE EQUIPOS
# Autor: Álvaro Leandro Gutiérrez Carranza
# ============================================================

# ------------------------------------------------------------
# INSTRUCCIONES ÁLVARO:
# 1. Crea registrar_equipo(lista): pide código, nombre, categoría.
# 2. Crea listar_disponibilidad(lista): muestra todos los equipos.
# 3. Crea consultar_por_categoria(lista): cuenta equipos por categoría.
# ------------------------------------------------------------
# PEGA TU CÓDIGO AQUÍ
import utilidades

def registrar_equipo(lista_equipos):
    print("\n--- REGISTRAR EQUIPO ---")
    codigo = input("Código del equipo: ")
    if not utilidades.validar_texto(codigo): return
    nombre = input("Nombre del equipo: ")
    categoria = input("Categoría (Laptop/Mouse/etc): ")
    lista_equipos.append({"codigo": codigo, "nombre": nombre, "categoria": categoria, "estado": "Disponible"})
    print("Equipo registrado.")

def listar_disponibilidad(lista_equipos):
    print("\n--- LISTA DE EQUIPOS ---")
    for eq in lista_equipos:
        print(f"[{eq['codigo']}] {eq['nombre']} - {eq['estado']}")

def consultar_por_categoria(lista_equipos):
    categoria = input("Ingrese categoría a consultar: ")
    count = sum(1 for eq in lista_equipos if eq["categoria"].lower() == categoria.lower() and eq["estado"] == "Disponible")
    print(f"Equipos disponibles en '{categoria}': {count}")
