# ============================================================
# LABORATORIO 5 - PERSISTENCIA DE DATOS
# ============================================================

import pickle
import os


ARCHIVO_TEXTO = "contactos.txt"
ARCHIVO_BINARIO = "contactos.dat"

# ------------------------------------------------------------
# ETAPA 1: ESCRITURA DE ARCHIVO DE TEXTO (Añadir sin sobrescribir)
# Autor: Cristian Omar Huamán Rojas
# ------------------------------------------------------------
def agregar_contacto():
    print("\n--- NUEVO CONTACTO ---")
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el telefono: ")
    
    with open(ARCHIVO_TEXTO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{telefono}\n")
    
    print(f"Contacto '{nombre}' guardado en {ARCHIVO_TEXTO}.")



# ------------------------------------------------------------
# ETAPA 2: LECTURA DE ARCHIVO DE TEXTO (Línea por línea)
# Autor: Álvaro Leandro Gutiérrez Carranza
# ------------------------------------------------------------

def leer_texto():
    print("\n--- LISTA DE CONTACTOS (TEXTO) ---")
    if not os.path.exists(ARCHIVO_TEXTO):
        print("El archivo no existe.")
        return
    with open(ARCHIVO_TEXTO, "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo.readlines(), 1):
            datos = linea.strip().split(",")
            if len(datos) == 2:
                print(f"{i}. Nombre: {datos[0]} | Teléfono: {datos[1]}")



# ------------------------------------------------------------
# ETAPA 3: PROCESAMIENTO Y BÚSQUEDA EN TEXTO
# Autor: Zinedine Michael Callirgos Cabanillas
# ------------------------------------------------------------

def buscar_contacto():
    print("\n--- BUSCAR CONTACTO ---")

    if not os.path.exists(ARCHIVO_TEXTO):
        print("No hay contactos registrados.")
        return

    busqueda = input("Ingrese el nombre a buscar: ").lower()
    encontrado = False

    with open(ARCHIVO_TEXTO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")

            if len(datos) == 2 and busqueda in datos[0].lower():
                print(f"Encontrado -> Nombre: {datos[0]} | Telefono: {datos[1]}")
                encontrado = True

    if not encontrado:
        print("No se encontro ningun contacto con ese nombre.")

# ------------------------------------------------------------
# ETAPA 4: MANEJO DE ARCHIVOS BINARIOS
# Autor: Anthony Rene Terraz Terrones
def guardar_binario():
    print("\n--- GUARDANDO EN BINARIO ---")
    if not os.path.exists(ARCHIVO_TEXTO):
        print("No hay contactos.")
        return
    contactos = []
    with open(ARCHIVO_TEXTO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 2:
                contactos.append({"nombre": datos[0], "telefono": datos[1]})
    with open(ARCHIVO_BINARIO, "wb") as archivo_bin:
        pickle.dump(contactos, archivo_bin)
    print("Guardado en binario.")

def leer_binario():
    print("\n--- LEYENDO BINARIO ---")
    if not os.path.exists(ARCHIVO_BINARIO):
        print("Archivo binario no existe.")
        return
    with open(ARCHIVO_BINARIO, "rb") as archivo_bin:
        contactos = pickle.load(archivo_bin)
        for c in contactos:
            print(f"Nombre: {c['nombre']} | Tel: {c['telefono']}")
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 5: MENÚ PRINCIPAL Y CONTROL DEL SISTEMA
# Autor: Juan Orlando Correa Flores
# ------------------------------------------------------------

def mostrar_menu():
    print("\n" + "=" * 45)
    print("   SISTEMA DE GESTIÓN DE CONTACTOS")
    print("=" * 45)
    print("1. Agregar nuevo contacto (Archivo de Texto)")
    print("2. Mostrar todos los contactos (Leer Texto)")
    print("3. Buscar contacto por nombre")
    print("4. Guardar contactos en Binario (.dat)")
    print("5. Mostrar contactos desde Binario")
    print("6. Salir")
    print("=" * 45)

def main():
    opcion = ""
    while opcion != "6":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1": 
            agregar_contacto() 
        elif opcion == "2": 
            leer_texto()        
        elif opcion == "3": 
            buscar_contacto()   
        elif opcion == "4": 
            guardar_binario()   
        elif opcion == "5": 
            leer_binario()      
        elif opcion == "6": 
            print("\nSaliendo del sistema.")
        else: 
            print("\nOpción inválida.")

if __name__ == "__main__":
    main()