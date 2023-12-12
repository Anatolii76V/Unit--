import pytest


class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        if not lst:
            return 0
        return sum(lst) / len(lst)

    def compare_lists(self):
        avg_list1 = self.calculate_average(self.list1)
        avg_list2 = self.calculate_average(self.list2)

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        elif avg_list2 > avg_list1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


# Тесты с использованием Pytest


@pytest.mark.parametrize("list1, list2, expected_result", [
    ([1, 2, 3], [4, 5, 6], "Второй список имеет большее среднее значение"),
    ([1, 2, 3], [1, 2, 3], "Средние значения равны"),
    ([10, 20, 30], [5, 5, 5], "Первый список имеет большее среднее значение"),
    ([], [], "Средние значения равны"),
])
def test_list_comparator(list1, list2, expected_result):
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == expected_result

# Проверка покрытия кода тестами
# Запуск тестов с покрытием:
# pytest --cov=your_script_name.py
