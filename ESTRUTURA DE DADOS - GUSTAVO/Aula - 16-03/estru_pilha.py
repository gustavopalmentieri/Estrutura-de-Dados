#IMPLEMENTAÇÃO NA ESTRUTURA DE PILHA

v = []

for i in range(5):

    vlr = int(input('Digite um valor: '))
    v.append(vlr)

for i in range(5):

    print(v[i], end = ' ')

print()

v.pop(len(v) -1) #CONFORME ANOTADO, 'POP' REMOVE O ÚLTIMO ITEM ADICIONADO A ESTRUTURA.

print(v)

