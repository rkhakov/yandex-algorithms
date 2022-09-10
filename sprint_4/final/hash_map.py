"""
ID: 69665480

ПРИНЦИП РАБОТЫ
    Класс HashMap реализует хеш таблицу по методу цепочек
    Хранение данных осуществляется в массиве `HashMap.map`
    Размер таблицы определяется в конструкторе, макимальный размер которого 10^5

    Хеш функция:
        Так как по условию задачи ключи и значения являются целочисленными,
        хеш определяется делением ключа по модулю на максимальный размер массива

    Хранение данных
        Данные в массиве хранятся с использованием связного списка `Node`
        Каждый объект содержит переданные ключ и значение,
        а также ссылку на следующий объект если таковой существует

    Добавление `HashMap.put`:
        Метод принимает 2 параметра ключ `key` и значение `value`
        По хешу ключа определяется индекс в массиве где будет хранится значение
        Если по этому индексу в массиве уже есть данные,
        Проходимся по каджому и сравниваем их ключи с переданным ключом
        Если они совпадают, обновляем `Node.value` переданным значением
        В остальных случаях создаем объект Node с ссылкой `Node.next_node` на текущий в массиве
        Таким образом, если там ничего не было, то добавится один объект без ссылок на другие `None`
        Если объект уже был, то новый будет ссылаться на предыдущий. Такой сценарий
        возможен при коллизиях, например если максимальный размер массива 10,
        то `key` == 1 или 11 будут указывать на один индекс, т.е 1

    Получение значения из хеш таблицы `HashMap.get`:
        Метод принимает один параметр (ключ),
        по хешу ключа получаем значение из массива
        Если полученный элемент не пустой,
        проходимся по всем элементам связного списка и сравниваем с переданным ключом.
        Возвращается значение найденого элемента

    Удаление `HashMap.delete`:
        Все также, получаем по хеш ключа элемент массива,
        Находим нужный элемент связного списка, и удаляем его,
        т.е меняем ссылку `next_node` у предыдущего элемента
        на ссылку следующего `next_node` элемента у текущего

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    n - Количество запросов
    k - Количество одновременно хранимых ключей в таблице
    m - Общее число корзин в таблицу

    В лучшем случае, когда корзина пустая или в ней только один ключ,
    запрос будет выполнен за константное врермя
    В худшем случае потребуется пройти по всем ключам в корзине

    Время работы всего алгоритма - O(1 + k/m)
        Зависит от коэффициента заполнения таблицы
    

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(k)
    k - Количество одновременно хранимых ключей в таблице
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    key: int
    value: int
    next_node: Optional["Node"] = None


class HashMap:
    def __init__(self) -> None:
        self.size: int = 102_023
        self.map: List[Optional[Node]] = [None] * self.size

    def put(self, key: int, value: int) -> None:
        hashed_key = self._hash(key)
        node = self.map[hashed_key]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next_node

        self.map[hashed_key] = Node(key=key, value=value, next_node=self.map[hashed_key])

    def get(self, key: int) -> Optional[int]:
        hashed_key = self._hash(key)
        node = self.map[hashed_key]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next_node

    def delete(self, key: int) -> Optional[int]:
        hashed_key = self._hash(key)
        prev_node = None
        node = self.map[hashed_key]
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.map[hashed_key] = node.next_node
                else:
                    prev_node.next_node = node.next_node
                    self.map[hashed_key] = prev_node
                return node.value
            prev_node, node = node, node.next_node

    def _hash(self, key: int) -> int:
        return key % self.size


def main() -> None:
    queries_num = int(input())
    hash_map = HashMap()
    for _ in range(queries_num):
        inputs = input().split()
        action = inputs[0]
        if action == "get":
            print(hash_map.get(int(inputs[1])))
        elif action == "put":
            hash_map.put(int(inputs[1]), int(inputs[2]))
        elif action == "delete":
            print(hash_map.delete(int(inputs[1])))


if __name__ == "__main__":
    main()
