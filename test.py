import unittest

from areaquadrada import area


class TestAreaRetangulo(unittest.TestCase):
    """
    Esta classe testa a area do retangulo
    """
    def test_area_do_triangulo(self):
        resultado = area(10, 50)
        esperado = 500
        self.assertEqual(resultado, esperado)

    def test_area_do_triangulo_com_base_negativa(self):
        resultado = area(-30, 10)
        esperado = 300
        self.assertEqual(resultado, esperado)

    def test_area_do_triangulo_com_altura_negativa(self):
        resultado = area(30, -10)
        esperado = 300
        self.assertEqual(resultado, esperado)

    def test_area_do_triangulo_com_base_e_altura_negativa(self):
        resultado = area(-30, -10)
        esperado = 300
        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()
