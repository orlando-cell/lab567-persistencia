# Laboratorio 7 - Recursividad

# ============================================================
# LABORATORIO 7 - RECURSIVIDAD
# Sistema de análisis de entregas digitales
# ============================================================
# Lista de 8 entregas simuladas (Datos iniciales - Orlando)
entregas = [
    {"codigo": "N001", "archivo": "tarea_final.pdf", "puntaje": 18},
    {"codigo": "N002", "archivo": "proyecto_v2.zip", "puntaje": 15},
    {"codigo": "N003", "archivo": "tarea1.docx", "puntaje": 20},
    {"codigo": "N004", "archivo": "examen_final.txt", "puntaje": 12},
    {"codigo": "N005", "archivo": "codigo_v2.py", "puntaje": 17},
    {"codigo": "N006", "archivo": "reporte.pdf", "puntaje": 14},
    {"codigo": "N007", "archivo": "manual_v2.pdf", "puntaje": 19},
    {"codigo": "N008", "archivo": "tarea_final_2.pdf", "puntaje": 16}
]

# ------------------------------------------------------------
# ETAPA 1: SUMATORIA RECURSIVA DE PUNTAJES
# Autor: Cristian Omar Huamán Rojas
# INSTRUCCIONES: Crea la función recursiva 'sumar_puntajes_recursivo(lista, indice)' 
# que sume los puntajes. Caso base: si indice == len(lista) retornar 0.
# ------------------------------------------------------------

# PEGA TU CÓDIGO AQUÍ



# ------------------------------------------------------------
# ETAPA 2: BÚSQUEDA RECURSIVA DE ESTUDIANTE
# Autor: Álvaro Leandro Gutiérrez Carranza
# INSTRUCCIONES: Crea la función recursiva 'buscar_estudiante_recursivo(lista, codigo, indice)'
# que retorne el diccionario si lo encuentra, o None si no existe.
# ------------------------------------------------------------

# PEGA TU CÓDIGO AQUÍ



# ------------------------------------------------------------
# ETAPA 3: CONTEO RECURSIVO DE PALABRAS CLAVE
# Autor: Zinedine Michael Callirgos Cabanillas
# INSTRUCCIONES: Crea 'contar_palabra_recursivo(lista, palabra, indice)'
# que cuente cuántos archivos contienen cierta palabra (ej. "final" o "v2").
# ------------------------------------------------------------

# PEGA TU CÓDIGO AQUÍ



# ------------------------------------------------------------
# ETAPA 4: FUNCIÓN RECURSIVA SIMPLE Y VALIDACIONES
# Autor: Anthony Rene Terraz Terrones
# INSTRUCCIONES: Crea 'factorial_recursivo(n)' o 'potencia_recursiva(base, exp)'
# Además, crea una función 'validar_entrada(valor)' que evite negativos o vacíos.
# ------------------------------------------------------------

# PEGA TU CÓDIGO AQUÍ



# ------------------------------------------------------------
# ETAPA 5: SOLUCIÓN ITERATIVA Y MENÚ PRINCIPAL
# Autor: Juan Orlando Correa Flores
# ------------------------------------------------------------

def sumar_puntajes_iterativo(lista):
    """Solución iterativa para comparar con la recursiva."""
    suma = 0
    for entrega in lista:
        suma += entrega["puntaje"]
    return suma

def mostrar_menu():
    print("\n" + "=" * 50)
    print("   ANÁLISIS DE ENTREGAS DIGITALES - RECURSIVIDAD")
    print("=" * 50)
    print("1. Sumar puntajes (Recursivo vs Iterativo)")
    print("2. Buscar código de estudiante (Recursivo)")
    print("3. Contar archivos por palabra clave (Recursivo)")
    print("4. Calcular Factorial (Recursivo Simple)")
    print("5. Salir")
    print("=" * 50)

def main():
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- SUMA DE PUNTAJES ---")
            suma_iter = sumar_puntajes_iterativo(entregas)
            print(f"Suma Iterativa (Orlando): {suma_iter}")
            print("*(La suma recursiva se activará cuando Cristian suba su parte)*")
     
        elif opcion == "2":
            print("\n--- BÚSQUEDA DE ESTUDIANTE ---")
            codigo = input("Ingrese código a buscar (ej. N003): ").upper()
            print("*(Búsqueda en espera de la función de Álvaro)*")
            
        elif opcion == "3":
            print("\n--- CONTEO DE PALABRAS CLAVE ---")
            palabra = input("Ingrese palabra clave (ej. 'final' o 'v2'): ").lower()
            print("*(Conteo en espera de la función de Zinedine)*")
            
        elif opcion == "4":
            print("\n--- FACTORIAL RECURSIVO ---")
            num = int(input("Ingrese un número entero: "))
            print("*(Factorial en espera de la función de Anthony)*")
            
        elif opcion == "5":
            print("\nSaliendo del sistema.")
        else:
            print("\nOpción inválida.")

if __name__ == "__main__":
    main()

