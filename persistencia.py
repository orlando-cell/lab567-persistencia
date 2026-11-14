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



# ------------------------------------------------------------
# ETAPA 2: LECTURA DE ARCHIVO DE TEXTO (Línea por línea)
# Autor: Álvaro Leandro Gutiérrez Carranza
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 3: PROCESAMIENTO Y BÚSQUEDA EN TEXTO
# Autor: Zinedine Michael Callirgos Cabanillas
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 4: MANEJO DE ARCHIVOS BINARIOS
# Autor: Anthony Rene Terraz Terrones
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