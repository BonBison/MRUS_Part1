import unittest
from calculator import power

# Создаем класс для тестирования функции power
class TestCalculator(unittest.TestCase):
    # Тестирование функции power с положительным показателем степени
    def test_power_positive_exponent(self):
        # Проверяем, что power(2, 3) равно 8
        self.assertEqual(power(2, 3), 8)
        # Проверяем, что power(3, 2) равно 9
        self.assertEqual(power(3, 2), 9)
        # Проверяем, что power(5, 1) равно 5
        self.assertEqual(power(5, 1), 5)

    # Тестирование функции power с отрицательным показателем степени
    def test_power_negative_exponent(self):
        # Проверяем, что power(2, -3) приблизительно равно 0.125
        self.assertAlmostEqual(power(2, -3), 0.125)
        # Проверяем, что power(3, -2) приблизительно равно 0.111111 с точностью до 5 знаков после запятой
        self.assertAlmostEqual(power(3, -2), 0.111111, places=5)
        # Проверяем, что power(5, -1) приблизительно равно 0.2
        self.assertAlmostEqual(power(5, -1), 0.2)

    # Тестирование функции power с показателем степени равным нулю
    def test_power_zero_exponent(self):
        # Проверяем, что power(2, 0) равно 1
        self.assertEqual(power(2, 0), 1)
        # Проверяем, что power(3, 0) равно 1
        self.assertEqual(power(3, 0), 1)
        # Проверяем, что power(5, 0) равно 1
        self.assertEqual(power(5, 0), 1)

if __name__ == '__main__':
    # Запускаем тестирование
    unittest.main()