import math

class CalculadoraDeAreas:

    # esse metodo calcula a area de um circulo dado o raio
    def calcularAreaCirculo(self, raio):
        if raio < 0:
            raise ValueError("O raio não pode ser negativo!")
        return math.pi * raio * raio

    # esse metodo calcula a area de um quadrado dado o comprimento do lado
    def calcularAreaQuadrado(self, lado):
        if lado < 0:
            raise ValueError("O lado não pode ser negativo")
        return lado * lado
