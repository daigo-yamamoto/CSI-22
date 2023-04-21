# Funcao que faz a somatoria das linhas da matriz

def soma_linha(matriz):
    return list(map(sum, matriz))


# Teste
# A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# print(soma_linha(A))