def primos():
    yield 2  # unico primo par
    divisor = 3
    dividendo = 3
    while True:
        if dividendo % divisor == 0:
            if dividendo == divisor:
                yield dividendo
            dividendo += 2  # Proximo impar
            divisor = 3
        elif divisor < dividendo:
            divisor += 2  # Proximo impar
        else:
            dividendo += 2  # Proximo impar

# Teste
# for primo in primos():
#     print(primo)
