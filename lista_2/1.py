def remove_tuplas_vazias(lista):
    lista_aux = []
    for tupla in lista:
        if len(tupla):
            lista_aux.append(tupla)
    return lista_aux

# Teste:
# print(remove_tuplas_vazias([(1,),(),(2,3),(4,5,6),(),(7,)]))
