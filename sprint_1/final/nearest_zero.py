# ID: 69343778
# Задача: Найти ближайшее расстояние элемента массива до 0
# Решение O(n):
#   1. Проходимся по массиву слева-направо, находим расстояние для чисел справа от 0
#   2. Проходим по массиву справа-налево, находим расстоние для чисел слева от 0
# Пример
#   => 5 0 7 4 8 0 2 3
#   1. 5 0 1 2 3 0 1 2
#   2. 1 0 1 2 1 0 1 2
from typing import List


def calc_distance(numbers: List[int], len_numbers: int) -> List[int]:
    if numbers[0] != 0:
        numbers[0] = len_numbers - 1

    for key in range(1, len_numbers):
        if numbers[key] != 0:
            numbers[key] = numbers[key - 1] + 1

    for key in range(len_numbers - 2, -1, -1):
        if numbers[key] != 0:
            min_value = min(numbers[key], numbers[key + 1] + 1)
            numbers[key] = min_value

    return numbers


def main():
    len_numbers: int = int(input())
    numbers: List[int] = [int(i) for i in input().split()]
    calc_distance(numbers, len_numbers)
    for number in numbers:
        print(number, end=' ')
    print()


if __name__ == "__main__":
    main()
