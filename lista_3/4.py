class Calculadora:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial

    def somar(self, valor):
        self.valor += valor

    @classmethod  # Metodo pertencente a classe e nao ao objeto
    def calcular_media(cls, valores):
        return sum(valores) / len(valores)

    @staticmethod  # Semelhantes ao método de classe, mas não recebem uma referência explícita à classe como argumento.
    def converter_para_binario(numero):
        return bin(numero)

