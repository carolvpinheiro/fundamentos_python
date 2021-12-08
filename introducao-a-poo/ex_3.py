# E como poderíamos definir um círculo? 
# Qual seu nome, atributos e comportamentos?

import math

PI = 3.14159


class Circulo:

    def __init__(self, circunferencia):
        self.circunferencia = circunferencia

    def calcular_raio(self):
        return self.circunferencia / (2 * PI)

    def calcular_area(self):
        print(PI * math.pow(self.calcular_raio, 2))
