lista=['1','1','2','3','4','4','5','1']
lista2=[]
lista2=lista[0:1]
for i in range(len(lista)):
    if lista[i] not in lista2:
        lista2.append(lista[i])
    print(lista2)