while True:
    opciones = 0
    menu = """ 
    ----Menu de Opciones
    1. Ingresar tu nombre
    2. Visualizar ejercicios
    3. Salir
    """
    print(menu)
    opciones = int(input("Elija una opcion por favor"))
    match opciones:
        case 1:
            nombre = input("Holi por favor ingresa tu nombre")
            print("Bienvenido al sistema ", nombre," que tengas un lindo dia")
        case 2:
            while True:
                    menuop = """
                             ----Bienvenido al menu de visualizacion----
                             ----1.Ejercicio numero 1
                             ----2.Ejercicio numero 2
                             ----3.Ejercicio numero 3
                             4.Ejercicio numero 4
                             5.Ejercicio numero 5
                             6.Ejercicio numero 6
                             7.Ejercicio numero 7
                             8.Ejercicio numero 8
                             9.Ejercicio numero 9
                             10.Ejercicio numero 10
                             11.Ejercicio numero 11
                             12.Salir
                             """
                    print(menuop)               
                    opcionesej = int(input("Por Favor Elija una opcion"))
                    match opcionesej:
                        case
        case 3:
            break
        case _:
            print("Por favor Ingrese una opcion valida")
            
            
            
def ejercicio1():
    encabezado = """¿Que imprime el codigo?
                        print("ab" * 3)
                """
    print(encabezado)
    print("La respuesta es: ","ab" * 3)

def ejercicio2():
    encabezado = """¿Qué imprime el siguiente código?
                        socio = {"nombre": "Ana", "saldo": 120}
                        print(socio.get("correo", "Sin correo"))
                """
    socio = {"nombre": "Ana", "saldo": 120}
    print(encabezado)
    print("La respuesta es: ",socio.get("correo", "Sin correo"))
    
def ejercicio3():
    encabezado = """¿Qué imprime el siguiente código?

                    print(int(9.99))
                """
    print(encabezado)
    print("La respuesta es: ",int(9.99))

def ejercicio4():
    encabezado = """¿Qué imprime el siguiente código?
    
                        texto = "TEC Azuay"
                        print(texto[4:7])
                """
    texto = "TEC Azuay"
    print(encabezado)
    print("La respuesta es: ",texto[4:7])
    
def ejercicio5():
    encabezado = """¿Qué imprime el siguiente código?

                    print(type(10.0))
                """
    print(encabezado)
    print("La respuesta es: ",type(10.0))

def ejercicio6():
    encabezado = """¿Cuántas veces se imprime «*» en el siguiente código?

                    for i in range(3):
                        for j in range(2):
                        print("*", end="")
                """
    contador = 0
    for i in range(3):
        for j in range(2):
            print("*", end="")
            contador =+1
    print(encabezado)
    print("La respuesta es: ",contador)
    

def ejercicio7():
    encabezado = """¿Qué imprime el siguiente código?

                        notas = {"Ana": 10, "Luis": 8}
                        for nombre, nota in notas.items():
                            print(f"{nombre}:{nota}", end=" ")
                """
    notas = {"Ana": 10, "Luis": 8}
    
    print(encabezado)
    print("La respuesta es: ")
    for nombre, nota in notas.items():
            print(f"{nombre}:{nota}", end=" ")
            
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
    print("La respuesta es: ",total)

def ejercicio9():
    encabezado = """¿Qué imprime el siguiente código?

                        for n in [1, 2, 3, 4]:
                            if n == 3:
                            break
                            print(n, end=" ")
                """
    print(encabezado)
    print("La respuesta es: ")
    for n in [1, 2, 3, 4]:
        if n == 3:
            break
        print(n, end=" ")

    
    

