import unittest
import math
from calculadora_areas import CalculadoraDeAreas

class TestCalculadoraDeAreas(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraDeAreas()

    def test_calcular_area_circulo(self):
        self.assertAlmostEqual(self.calc.calcularAreaCirculo(1), math.pi)
        self.assertAlmostEqual(self.calc.calcularAreaCirculo(0), 0)
        self.assertRaises(ValueError, self.calc.calcularAreaCirculo, -1)

    def test_calcular_area_quadrado(self):
        self.assertEqual(self.calc.calcularAreaQuadrado(2), 4)
        self.assertEqual(self.calc.calcularAreaQuadrado(0), 0)
        self.assertRaises(ValueError, self.calc.calcularAreaQuadrado, -2)

    def test_calcular_area_retangulo(self):
        self.assertEqual(self.calc.calcularAreaRetangulo(2, 3), 6)
        self.assertEqual(self.calc.calcularAreaRetangulo(0, 3), 0)
        self.assertRaises(ValueError, self.calc.calcularAreaRetangulo, -2, 3)
        self.assertRaises(ValueError, self.calc.calcularAreaRetangulo, 2, -3)
        self.assertRaises(ValueError, self.calc.calcularAreaRetangulo, -2, -3)

if __name__ == '__main__':
    unittest.main()
