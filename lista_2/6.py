def inverte_lista(lista):
    for i in range(len(lista) - 1, -1, -1):
        yield lista[i]


# Teste
# for elemento in inverte_lista([1, 2, 3, 4, 5, 6, 7, 8]):
#     print(elemento)
