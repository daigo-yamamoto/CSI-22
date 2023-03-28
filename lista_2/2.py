def media_das_tuplas(entrada):
    lista = []
    for tupla in entrada:
        lista.append(sum(tupla) / len(tupla))

    return tuple(lista)

# Teste
# print(media_das_tuplas(((2,3,4),(3,4,5,6),(2,4),(4,8,9))))

# Note que no exemplo dado no enunciado, a funcao retorna a metade da soma dos valores da tupla e nao a media
# gerando a seguinte funcao:

def metade_das_tuplas(entrada):
    lista = []
    for tupla in entrada:
        lista.append(sum(tupla) / 2)

    return tuple(lista)

# Teste
# print(metade_das_tuplas(((2,3,4),(3,4,5,6),(2,4),(4,8,9))))