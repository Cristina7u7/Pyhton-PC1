#Programa que lea dos números por teclado y que permite elegir entre 3 opciones en un menú:
 #Mostrar una suma de los dos números
 #Mostrar una resta de los dos números (el primero menos el segundo)
 #Mostrar una multiplicación de los dos números
 #En caso de introducir una opción inválida, el programa informará de que no es correcta.
menu=""""
    Bienvenidos a Python 
    1. Sumar dos números
    2. Resta de los dos números, el primero menos el segundo
    3.Multiplicación de dos números
    4. Salir
"""
print(menu)
opcion=int(input("Elige tu opción: "))
if opcion==1:
    numberOne=float(input("Ingrese número 1: "))
    numberTwo=float(input("Ingrese númeroo 2: "))
    resultado=numberOne+numberTwo
    print(f"La suma es {resultado}")
elif opcion ==2:
    numberOne=float(input("Ingrese número 1: "))
    numberTwo=float(input("Ingrese número 2: "))
    resultado=numberOne-numberTwo
    print(f"La resta es {resultado}")
elif opcion==3:
    numberOne=float(input("Ingrese número 1: "))
    numberTwo=float(input("Ingrese número 2: "))
    resultado=numberOne*numberTwo
    print(f"La multiplicación es {resultado}")
elif opcion ==4:
    print("Hasta luego")
else:
    print("Opción no valida")