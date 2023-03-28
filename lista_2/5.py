def multiplica_matriz(matriz1, matriz2):
    # Verificando se eh possivel executar essa operacao
    if len(matriz1[0]) != len(matriz2):
        return None

    # Montando a matriz com zeros do tamnaho do resultado
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

# Teste
#A = [[2,3],
#     [4,6]]
#
#B = [[1,3,0],
#     [2,1,1]]
#
#print(multiplica_matriz(A, B))
