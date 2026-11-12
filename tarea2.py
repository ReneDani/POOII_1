def ejercicio1():
    encabezado = """¿Qué imprime el código?
    print("ab" * 3)
    """
    print(encabezado)
    print("La respuesta es:", "ab" * 3)

def ejercicio2():
    encabezado = """¿Qué imprime el siguiente código?
    socio = {"nombre": "Ana", "saldo": 120}
    print(socio.get("correo", "Sin correo"))
    """
    socio = {"nombre": "Ana", "saldo": 120}
    print(encabezado)
    print("La respuesta es:", socio.get("correo", "Sin correo"))

def ejercicio3():
    encabezado = """¿Qué imprime el siguiente código?
    print(int(9.99))
    """
    print(encabezado)
    print("La respuesta es:", int(9.99))

def ejercicio4():
    encabezado = """¿Qué imprime el siguiente código?
    texto = "TEC Azuay"
    print(texto[4:7])
    """
    texto = "TEC Azuay"
    print(encabezado)
    print("La respuesta es:", texto[4:7])

def ejercicio5():
    encabezado = """¿Qué imprime el siguiente código?
    print(type(10.0))
    """
    print(encabezado)
    print("La respuesta es:", type(10.0))

def ejercicio6():
    encabezado = """¿Cuántas veces se imprime «*» en el siguiente código?
    for i in range(3):
        for j in range(2):
            print("*", end="")
    """
    print(encabezado)
    contador = 0
    for i in range(3):
        for j in range(2):
            print("*", end="")
            contador += 1  # Corregido: antes decía =+ 1
    print("\nLa respuesta es:", contador)

def ejercicio7():
    encabezado = """¿Qué imprime el siguiente código?
    notas = {"Ana": 10, "Luis": 8}
    for nombre, nota in notas.items():
        print(f"{nombre}:{nota}", end=" ")
    """
    notas = {"Ana": 10, "Luis": 8}
    print(encabezado)
    print("La respuesta es: ", end="")
    for nombre, nota in notas.items():
        print(f"{nombre}:{nota}", end=" ")
    print()  # Salto de línea para que no se pegue el menú

def ejercicio8():
    encabezado = """¿Qué imprime el siguiente código?
    total = 0
    n = 1
    while n <= 5:
        total += n
        n += 1
    print(total)
    """
    total = 0
    n = 1
    while n <= 5:
        total += n
        n += 1
    print(encabezado)
    print("La respuesta es:", total)

def ejercicio9():
    encabezado = """¿Qué imprime el siguiente código?
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")
    """
    print(encabezado)
    print("La respuesta es: ", end="")
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")
    print()  # Salto de línea para que no se pegue el menú

def ejercicio10():
    encabezado = """¿Qué imprime el siguiente código?
    for x in [2, 4, 6]:
        if x == 7:
            print("Encontrado")
            break
    else:
        print("No encontrado")
    """
    print(encabezado)
    print("La respuesta es: ", end="")
    for x in [2, 4, 6]:
        if x == 7:
            print("Encontrado")
            break
    else:
        print("No encontrado")


# --- PROGRAMA PRINCIPAL ---
while True:
    menu = """
    ---- Menú de Opciones ----
    1. Ingresar tu nombre
    2. Visualizar ejercicios
    3. Salir
    """
    print(menu)
    opciones = int(input("Elija una opción por favor: "))

    match opciones:
        case 1:
            nombre = input("Holi, por favor ingresa tu nombre: ")
            print(f"Bienvenido al sistema {nombre}, que tengas un lindo día.")

        case 2:
            while True:
                menuop = """
                ---- Bienvenido al menú de visualización ----
                1. Ejercicio número 1
                2. Ejercicio número 2
                3. Ejercicio número 3
                4. Ejercicio número 4
                5. Ejercicio número 5
                6. Ejercicio número 6
                7. Ejercicio número 7
                8. Ejercicio número 8
                9. Ejercicio número 9
                10. Ejercicio número 10
                11. Ejercicio número 11
                12. Salir al menú principal
                """
                print(menuop)
                opcionesej = int(input("Por favor elija una opción: "))

                match opcionesej:
                    case 1:
                        ejercicio1()
                    case 2:
                        ejercicio2()
                    case 3:
                        ejercicio3()
                    case 4:
                        ejercicio4()
                    case 5:
                        ejercicio5()
                    case 6:
                        ejercicio6()
                    case 7:
                        ejercicio7()
                    case 8:
                        ejercicio8()
                    case 9:
                        ejercicio9()
                    case 10:
                        ejercicio10()
                    case 11:
                        print("El ejercicio 11 aún no está definido.")
                    case 12:
                        print("Regresando al menú principal...")
                        break
                    case _:
                        print("Por favor ingrese una opción válida (1-12).")

        case 3:
            print("¡Hasta luego!")
            break

        case _:
            print("Por favor ingrese una opción válida (1-3).")

