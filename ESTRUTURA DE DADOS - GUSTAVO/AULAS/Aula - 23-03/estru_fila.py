fila = []

i = 0

#ENQUEUE
while i < 5:

    vlr = int(input("Digite um valor: "))
    fila.append(vlr)
    i = i + 1


print(fila)


#DEQUEUE

fila.pop(0)

print(fila)

