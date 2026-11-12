#Definicion de Funciones
def saludar ():
    print("Hola mi nombre es Rene Dominguez")
    
saludar()
#Funcion con parametros
# def calcular_edad (anio_naci,anio_actual):
    
#     edad = anio_actual - anio_naci
#     print("La edad de la persona es: ",edad)

# anionaci = int(input("Ingrese su año de nacimiento: "))
# anioactu = int(input("Ingrese el año actual: "))
# calcular_edad (anionaci,anioactu)

#Funciones con retorno
def calcular_IVA (precio_p,IVA_Valor):
    
    return precio_p * IVA_Valor

resultado = calcular_IVA(10,0.15)
resultado = calcular_IVA(100,0.14)
print("El IVA es : ",resultado)
#Funciones con listas
def par_o_impar(numeros):
    for i in numeros:
        if i % 2 ==0:
            print(i)
            print("El numero es par")
        else:
            print(i)
            print("El numero es impar")

lista_numeros = [0,1,2,3,4,5,6,7,8,9]
lista_numeros2 = range(5,0,-1)
print(lista_numeros2, end=",")
par_o_impar(lista_numeros2 )
#Funciones con  tuplas
def suma_numeros(*a):
    return sum(a)

tupla =(1,2,3,4,5,6,8,9)
print("La suma de los elementos es: ",suma_numeros(*tupla))

#Funciones con diccionarios
def estudiantes(**listaestudiante):
    sumaedad = 0
    for nombre,edad in listaestudiante.items():
        print("El estudiantes: ",nombre," Tiene :",edad," años")
        sumaedad = edad+sumaedad
    print("La Suma de las edades es: ",sumaedad)
        
estudiantes(Juan=20,Carlos=30,Maria=20,Paula=18)


