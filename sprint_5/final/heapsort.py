"""
ID: 70246381
ПРИНЦИП РАБОТЫ:
    Первым этапом необходимо из массива сформировать сортирующее дерево
    Левый и правый потомок элемента i массива определяются по формуле
    Левый: i * 2 + 1
    Правый: i * 2 + 2
    При проходе по массиву справа-налево и перемещая наибольший потомок в левую часть
    В результате самый первый элемент массива и будет максимальным

    Вторым этапом, так как максимальный элемент находится на первом месте в массиве,
    меняем его с последним элементом.
    После перестановки элементов местами, небоходимо повторить просейку, 
    для восстановления сортирующего дерева. 
    Действия повторяются пока не дойдем до конца массива

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    O(log n) - однократная просейка
    O(n log n) - Первый этап. Для каждого элемента в массиве делаем просейку чтобы построить кучу
    O(n log n) - Второй этап. Перемещение максимумов и просейка для оставшейся части массива
    Итог: O(n log n) + O(n log n) = O(n log n)

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(1) - Меняется сразу исходный массив, без использования доп. памяти
"""
from __future__ import annotations
from typing import NamedTuple, List, Any, TypeVar

T = TypeVar("T")


def __siftdown(data: List[Any], start: int, end: int):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        if data[root] > data[child]:
            break

        data[root], data[child] = data[child], data[root]
        root = child


def heapsort(data: List[T]) -> List[T]:
    for start in range((len(data) - 2) // 2, -1, -1):
        __siftdown(data, start, len(data) - 1)
    
    for end in range(len(data) - 1, 0, -1): 
        data[end], data[0] = data[0], data[end]
        __siftdown(data, 0, end - 1)
    return data


class User(NamedTuple):
    login: str
    solved: int
    fines: int

    def key(self):
        return -self.solved, self.fines, self.login

    def __lt__(self, other: User) -> bool:
        return self.key() < other.key()
    
    def __gt__(self, other: User) -> bool:
        return self.key() > other.key()


def main():
    users = []
    for _ in range(int(input())):
        login, solved, fines = input().split()
        users.append(User(
            login=login,
            solved=int(solved),
            fines=int(fines),
        ))

    for user in heapsort(users):
        print(user.login)


if __name__ == "__main__":
    main()
