# -------------------- MENÚ PRINCIPAL --------------------

# Lista que almacena todas las palabras que el usuario
# ha intentado ingresar durante la sesión.
palabras_intentadas = []

while True:
    print("\n" + "=" * 50)
    print("       PROYECTO FINAL - PYTHON")
    print("=" * 50)
    print("1. Validar longitud de una palabra")
    print("2. Determinar cuadrante")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    # -------------------- RETO 1 --------------------

    if opcion == "1":
        print("\n--- Validación de palabra ---")

        # Variable booleana que controla cuándo termina el ciclo.
        palabra_correcta = False

        while not palabra_correcta:
            palabra = input(
                "Escriba una palabra que tenga entre 4 y 8 letras: "
            )

            # Agregamos cada palabra ingresada a la lista.
            palabras_intentadas.append(palabra)

            cantidad_letras = len(palabra)

            if cantidad_letras < 4:
                print("¡Palabra incorrecta!")
                print(
                    "La palabra tiene menos de 4 letras. "
                    "Inténtalo de nuevo.\n"
                )

            elif cantidad_letras > 8:
                print("¡Palabra incorrecta!")
                print(
                    "La palabra tiene más de 8 letras. "
                    "Inténtalo de nuevo.\n"
                )

            else:
                print(
                    "¡Palabra correcta! "
                    "Tiene entre 4 a 8 letras.\n"
                )
                palabra_correcta = True

        # Mostramos todos los intentos realizados.
        print("Registro de palabras ingresadas:")
        print(palabras_intentadas)

    # -------------------- RETO 2 --------------------

    elif opcion == "2":
        print("\n--- Determinación de cuadrante ---")
        print("Ingrese las coordenadas (X, Y). Ninguna puede ser 0.")

        # Tupla que almacena los nombres de los cuatro cuadrantes.
        # Se utiliza una tupla porque los nombres no necesitan
        # modificarse durante la ejecución del programa.
        cuadrantes = (
            "Cuadrante I",
            "Cuadrante II",
            "Cuadrante III",
            "Cuadrante IV"
        )

        numero_1 = 0
        numero_2 = 0

        # El ciclo continúa mientras alguna coordenada sea 0.
        while numero_1 == 0 or numero_2 == 0:

            try:
                # input() recibe el dato como texto.
                # int() convierte el texto en un número entero.
                numero_1 = int(input("Ingrese el primer número (X): "))

                if numero_1 == 0:
                    print(
                        "Error: El número 0 no es válido en las coordenadas."
                    )
                    print("Intente de nuevo.\n")
                    continue

                numero_2 = int(input("Ingrese el segundo número (Y): "))

                if numero_2 == 0:
                    print(
                        "Error: El número 0 no es válido en las coordenadas."
                    )
                    print("Intente de nuevo.\n")

                    # Reiniciamos X para volver a solicitar
                    # las dos coordenadas.
                    numero_1 = 0

            except ValueError:
                print(
                    "Error: Debe ingresar únicamente números enteros."
                )
                print("Intente de nuevo.\n")

                # Reiniciamos las coordenadas para repetir el proceso.
                numero_1 = 0
                numero_2 = 0

        # Utilizamos los índices de la tupla para mostrar
        # el nombre correspondiente al cuadrante.
        if numero_1 > 0 and numero_2 > 0:
            print(cuadrantes[0], "(++)")

        elif numero_1 < 0 and numero_2 > 0:
            print(cuadrantes[1], "(-+)")

        elif numero_1 < 0 and numero_2 < 0:
            print(cuadrantes[2], "(--)")

        elif numero_1 > 0 and numero_2 < 0:
            print(cuadrantes[3], "(+-)")

    # -------------------- SALIR --------------------

    elif opcion == "3":
        print("\nPrograma finalizado.")
        break

    # -------------------- OPCIÓN NO VÁLIDA --------------------

    else:
        print("\nOpción no válida. Intente nuevamente.")

