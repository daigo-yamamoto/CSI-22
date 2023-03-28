def apenas_alphanumericos(lista):
    lista_aux = []
    for palavra in lista:
        flag = False
        for letra in palavra:
            if letra.isalnum():
                flag = True
        if flag:
            lista_aux.append(palavra)

    return lista_aux

# Teste
# print(apenas_alphanumericos(['abc', '#abc', '#$%']))