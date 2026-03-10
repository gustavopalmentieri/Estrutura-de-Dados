m = [ #QUALQUER ELEMENTO DE UMA MARIZ TEM DOIS ÍNDICE - LINHA E COLUNA

    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [2, 4, 6]

    ]

for l in range(4): #RANGE QUE PASSA PELAS LINHAS - QUANTIDADE
    

    for c in range(3): #RANGE QUE PASSA PELAS COLUNAS - QUANTIDADE

        print(m[l][c], end = ' ')

    print() #PRINT EM BRANCO