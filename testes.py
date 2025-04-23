import unittest
from conversor import celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius, fahrenheit_para_kelvin

class TestConversor(unittest.TestCase):


    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)


    def test_celsius_para_kelvin(self):
        self.assertEqual(celsius_para_kelvin(0), 273.15)
        self.assertEqual(celsius_para_kelvin(100), 373.15)


    def test_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0)
        self.assertEqual(fahrenheit_para_celsius(212), 100)


    def test_fahrenheit_para_kelvin(self):
        self.assertEqual(fahrenheit_para_kelvin(32), 273.15)
        self.assertEqual(fahrenheit_para_kelvin(212), 373.15)


    def test_valor_invalido(self):
        with self.assertRaises(ValueError):
            celsius_para_fahrenheit("inválido")

if __name__ == "__main__":
    unittest.main()
