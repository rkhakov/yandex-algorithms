from typing import List, Optional


class Deque:
    def __init__(self, max_size: int):
        self._queue: List[Optional[int]] = [None] * max_size
        self._right_index: int = -1
        self._left_index: int = 0
        self._size: int = 0

    def can_push(self) -> bool:
        """
        Проверяет можно ли добавить новый элемент в дек

        Новое значение можно добавить только
        если текущий размер дека меньше максимального размера
        """
        return self._size < len(self._queue)

    def is_empty(self) -> bool:
        return self._size == 0

    def push_back(self, value: int) -> bool:
        if not self.can_push():
            return False
        self._right_index = (self._right_index + 1) % len(self._queue)
        self._queue[self._right_index] = value
        self._size += 1
        return True

    def push_front(self, value: int) -> bool:
        if not self.can_push():
            return False
        self._left_index = (self._left_index - 1) % len(self._queue)
        self._queue[self._left_index] = value
        self._size += 1
        return True

    def pop_back(self) -> Optional[int]:
        """ Извлекает последний элемент дэка (значение по индексу `_right_index`)
        Значения заменяется на None для наглядности удаления элемента """
        if self.is_empty():
            return None
        value = self._queue[self._right_index]
        self._queue[self._right_index] = None
        self._right_index = (self._right_index - 1) % len(self._queue)
        self._size -= 1
        return value

    def pop_front(self) -> Optional[int]:
        """ Извлекает первый элемент дэка (значение по индексу `_left_index`)
        Значения заменяется на None для наглядности удаления элемента """
        if self.is_empty():
            return None
        value = self._queue[self._left_index]
        self._queue[self._left_index] = None
        self._left_index = (self._left_index + 1) % len(self._queue)
        self._size -= 1
        return value

    def __str__(self) -> str:
        return " ".join([str(val) for val in self._queue])

    def __len__(self) -> int:
        return self._size


def main():
    cmd_count = int(input())
    deque_max_size = int(input())
    deck = Deque(deque_max_size)
    for _ in range(cmd_count):
        cmd = input().split()

        action = cmd[0]
        value = int(cmd[1]) if len(cmd) == 2 else None

        if action == "push_back" and value is not None:
            if not deck.push_back(value):
                print("error")
        elif action == "push_front" and value is not None:
            if not deck.push_front(value):
                print("error")
        elif action == "pop_front":
            val = deck.pop_front()
            print(val) if val is not None else print("error")
        elif action == "pop_back":
            val = deck.pop_back()
            print(val) if val is not None else print("error")


if __name__ == "__main__":
    main()
