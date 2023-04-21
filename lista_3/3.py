from abc import ABC, abstractmethod

class Letras(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class A(Letras):
    def emitir_som(self):
        return "A"


class S(Letras):
    def emitir_som(self):
        return "S"


class F(Letras):
    def emitir_som(self):
        return "F"


letras = [A(), S(), F()]

for letra in letras:
    print(letra.emitir_som())