import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        # Executa no 1° parametro e o 2° e o resultado esperado
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(0, '11')

    def test_subtrai_10_e_5_deve_retornar_5(self):
        self.assertEqual(subtrai(10, 5), 5)

    def test_subtrai_5_e_10_deve_retornar_5(self):
        self.assertEqual(subtrai(5, 10), -5)

    def test_subtrai_varias_saidas(self):
        x_y_saidas = (
            (50, 25, 25),
            (25, 100, -75),
            (1.5, 0.6, 0.9),
            (15, 10, 5),
            (50, 50, 0),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

unittest.main(verbosity=2)