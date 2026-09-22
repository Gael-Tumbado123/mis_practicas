lista = [9.7, 8.9, 9.1, 7.6, 8.5, 9.3, 10, 8.8, 9.2, 9.5, 6.7, 7.5, 7.9, 9.9, 8.1]
print(lista)
swapped = True
while swapped:
    swapped = False
for i in range(len(lista)):
    for x in range(len(lista)-1):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
            swapped = True
print("orden acendente: ", lista)
swapped = True
while swapped:
    swapped = False
for i in range(len(lista)):
    for x in range(len(lista)-1):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=aux
            swapped = True
print("orden decendente: ", lista)