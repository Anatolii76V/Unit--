import pytest


# Функция even_odd_number проверяет, является ли число четным или нечетным
def even_odd_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Параметризированный тест с помощью pytest для проверки различных случаев
@pytest.mark.parametrize("number, expected_result", [
    (2, "Even"),
    (0, "Even"),
    (-4, "Even"),
    (100, "Even"),
    (3, "Odd"),
    (7, "Odd"),
    (-5, "Odd"),
    (101, "Odd"),
    (-6, "Even"),
    (-9, "Odd"),
    (-11, "Odd"),
    (11, "Odd"),
])
def test_even_odd_number(number, expected_result):
    # Проверка, что функция возвращает ожидаемый результат для каждого входного числа
    assert even_odd_number(number) == expected_result
