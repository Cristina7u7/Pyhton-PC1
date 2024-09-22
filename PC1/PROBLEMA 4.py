# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
 #pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
 #puede ser calculada de la siguiente forma
n=int(input("Introduzca el número entero positivo: "))

if n>0:
        suma=n*(n+1)/2
        print(f"La suma de los {n} primeros enteros positivos es: {suma}")
if n<0:
        print("Introduzca solo número entero positivo")
