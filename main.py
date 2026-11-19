# Modulo principal

# ============================================================
# LABORATORIO 6 - SISTEMA MODULAR DE PRÉSTAMOS (LabTech)
# Archivo Principal (main.py)
# Autor: Juan Orlando Correa Flores
# ============================================================

import utilidades
import gestion
import prestamos
import reportes

# Lista global para almacenar los equipos
lista_equipos = []

def mostrar_menu():
    print("\n" + "=" * 50)
    print("   SISTEMA DE PRÉSTAMOS - LABTECH")
    print("=" * 50)
    print("1. Registrar nuevo equipo")
    print("2. Registrar préstamo de equipo")
    print("3. Devolver equipo")
    print("4. Listar disponibilidad de equipos")
    print("5. Consultar cantidad por categoría")
    print("6. Generar reporte general (Anthony)")
    print("7. Salir")
    print("=" * 50)

def main():
    opcion = ""
    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            gestion.registrar_equipo(lista_equipos)
        elif opcion == "2":
            prestamos.registrar_prestamo(lista_equipos)
        elif opcion == "3":
            prestamos.devolver_equipo(lista_equipos)
        elif opcion == "4":
            gestion.listar_disponibilidad(lista_equipos)
        elif opcion == "5":
            gestion.consultar_por_categoria(lista_equipos)
        elif opcion == "6":
            reportes.generar_reporte(lista_equipos)
        elif opcion == "7":
            print("\nSaliendo del sistema. ¡Hasta luego!")
        else:
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()