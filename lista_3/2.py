class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")


class D(B, C):
    pass


d = D()
d.method() # Output: "B"

# Note que foi escolhido o B, pois pelo MRO, a ordem de prioridade é D, B, C, A.

# class D(C, B):
#     pass

# A saida seria C e nao B, pois mudamos a prioridade das classes
