m = []

v1 = []
v2 = []
v3 = []

for i in range(3):

    vlr = int(input('Digite um valor para o vetor 1: '))
    v1.append(vlr)

m.append(v1)

for i in range(3):

    vlr2 = int(input('Digite um valor para o vetor 2: '))
    v2.append(vlr2)

m.append(v2)

for i in range(3):

    vlr3 = int(input('Digite um valor para o vetor 3: '))
    v3.append(vlr3)

m.append(v3)

for i in m:

    print(i)

