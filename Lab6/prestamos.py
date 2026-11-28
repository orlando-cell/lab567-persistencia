def registrar_prestamo(lista_equipos):
    print("\n--- REGISTRAR PRESTAMO ---")
    codigo = input("Codigo del equipo a prestar:") ")

    for eq in lista_equipos:
        if eq["codigo"] == codigo:
            if eq["estado"] == "Prestado":
                print("Error: El equipo ya esta prestado.")
                return

            eq["estado"] = "Prestado"
            print(f"Equipo {eq['nombre']} prestado con exito.")
            return

    print("Codigo de equipo no existe.")


def devolver_equipo(lista_equipos):
    print("\n--- DEVOLVER EQUIPO ---")
    codigo = input("Codigo del equipo a devolver: ")

    for eq in lista_equipos:
        if eq["codigo"] == codigo:
            eq["estado"] = "Disponible"
            print("Equipo devuelto.")
            return

    print("Equipo no encontrado.")