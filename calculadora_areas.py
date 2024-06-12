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

    # esse metodo calcula a area de um retangulo dado o comprimento e a largura
    def calcularAreaRetangulo(self, comprimento, largura):
        if comprimento < 0 or largura < 0:
            raise ValueError("O comprimento e a largura não podem ser negativos")
        return comprimento * largura

