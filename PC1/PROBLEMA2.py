#PREGUNTAR AL USUARIO CUANTO FUE SU CONSUMO Y QUE PORCENTAJE DE PROPINA DESEA DEJAR AL MESERO
consumo=float(input("¿Cuánto fue su consumo? "))
descuento=float(input("¿Qué porcentaje de propina quiere dejarle al meserx? "))
propina=consumo*descuento/100
print(f"La propina que dejará es: {propina}")
