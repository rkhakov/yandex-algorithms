# ID: 69291228

# Задача: Найти максимальное количество баллов смогут набрать 2 игрока
#        Если будут нажимать на клавишу 1..9 последовательно
#        так чтобы покрыть все имеющиеся из доступных,
#        при условии что они могут нажимать каждый не более `player_max_keys` клавиш

# Решение
# Для каждой цифры 1..9 считаем количество имеющихся в массиве цифр
# Если оно входит в диапазон доступных, увеличиваем счетчик баллов

# Временная сложность:
#   O(9*16) -> O(1):
#       9 - клавиши от 1..9
#       16 - количество доступных цифр `available_keys`. Доступные цифры
#           это матрица 4x4 (16)
#   Сложность данного алгоритма можно представить как O(1),
#   так как асимтотическая сложность не меняется в завимости от принимаемых данных

# Пространственная сложность:
#   O(1): Дополнительная память не используется
from typing import List


def get_max_points(available_keys: List[str], player_max_keys: int):
    """Возвращает максимальное количество баллов,
    которые смогут набрать 2 игрока"""
    max_keys_pressed: int = player_max_keys * 2

    points = 0
    for key in range(1, 10):
        key_count = available_keys.count(str(key))
        if 1 <= key_count <= max_keys_pressed:
            points += 1

    return points


def main():
    player_max_keys: int = int(input())
    available_keys: List[str] = []
    for _ in range(4):
        available_keys.extend(list(input()))

    print(get_max_points(available_keys, player_max_keys))


if __name__ == "__main__":
    main()
