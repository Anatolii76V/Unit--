import pytest


# Функция, которая проверяет, попадает ли число в интервал (25; 100)
def check_number_in_interval(number):
    return 25 < number < 100


# Параметризированный тест с использованием pytest для проверки различных входных значений
@pytest.mark.parametrize("number, expected_result", [
    (30, True),
    (50, True),
    (99, True),
    (10, False),
    (24, False),
    (101, False),
    (150, False),
    (25, False),
    (100, False),
])
def test_check_number_in_interval(number, expected_result):
    # Проверка, что результат функции соответствует ожидаемому результату для каждого входного числа
    assert check_number_in_interval(number) == expected_result
