def mesmas_letras(palavra1, palavra2):
    for letra in palavra1:
        if letra not in palavra2:
            return False
    return True

# Teste
# print(mesmas_letras('abc', 'abcabcab'))
# print(mesmas_letras('abc', 'ababab'))
