#Crearemos un programa donde la empresa preguntará al usuario la edad del cliente y mostrar el precio de entrada
edad=int(input("Escriba su edad: "))

if edad<4:
    print('¡Su entrada es gratis!')
elif edad<=18:
    precio=5
    print('Su entrada cuesta $5')
else:
    precio=10
    print('Su entrada cuesta $10')