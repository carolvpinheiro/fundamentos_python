#  Como poderíamos modelar um objeto retângulo?

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        print((self.base * 2) + (self.altura * 2))

    def calcular_area(self):
        print(self.base * self.altura)
