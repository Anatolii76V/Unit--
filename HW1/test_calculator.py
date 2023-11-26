import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_calculate_discount(self):
        calculator = Calculator()

        # Проверка корректного расчета скидки
        self.assertEqual(calculator.calculate_discount(100, 10), 90)
        self.assertEqual(calculator.calculate_discount(200, 20), 160)

        # Проверка выброса исключения при недопустимых аргументах
        with self.assertRaises(ArithmeticError):
            calculator.calculate_discount(-50, 10)  # отрицательная сумма покупки
        with self.assertRaises(ArithmeticError):
            calculator.calculate_discount(100, -10)  # отрицательный процент скидки
        with self.assertRaises(ArithmeticError):
            calculator.calculate_discount(100, 110)  # процент скидки больше 100

    def test_calculation_addition(self):
        result = Calculator.calculation(5, 3, '+')
        self.assertEqual(result, 8)

    def test_calculation_subtraction(self):
        result = Calculator.calculation(10, 4, '-')
        self.assertEqual(result, 6)

    def test_calculation_multiplication(self):
        result = Calculator.calculation(6, 7, '*')
        self.assertEqual(result, 42)

    def test_calculation_division(self):
        result = Calculator.calculation(15, 3, '/')
        self.assertEqual(result, 5)

    def test_calculation_division_by_zero(self):
        with self.assertRaises(ArithmeticError):
            Calculator.calculation(10, 0, '/')

    def test_calculation_invalid_operator(self):
        with self.assertRaises(ValueError):
            Calculator.calculation(8, 2, '%')  # недопустимый оператор

    def test_calculate_discount_valid_input(self):
        result = Calculator.calculate_discount(100, 10)
        self.assertEqual(result, 90)

    def test_calculate_discount_edge_cases(self):
        # Проверка на ноль и на крайние значения процента скидки
        result_zero_discount = Calculator.calculate_discount(200, 0)
        result_hundred_discount = Calculator.calculate_discount(500, 100)
        self.assertEqual(result_zero_discount, 200)
        self.assertEqual(result_hundred_discount, 0)

    def test_calculate_discount_negative_input(self):
        with self.assertRaises(ArithmeticError):
            Calculator.calculate_discount(-50, 10)  # отрицательная сумма покупки
        with self.assertRaises(ArithmeticError):
            Calculator.calculate_discount(100, -10)  # отрицательный процент скидки
        with self.assertRaises(ArithmeticError):
            Calculator.calculate_discount(100, 110)  # процент скидки больше 100


if __name__ == '__main__':
    unittest.main()
