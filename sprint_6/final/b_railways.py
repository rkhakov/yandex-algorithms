"""
ID: 72924923

ПРИНЦИП РАБОТЫ:
    Определяем наличие циклов для каждой вершины графа
    Для этого создаем отдельный массив где будем помечать вершины в которых уже побывали
    Вершины могут иметь следющие состояния:
        - NOT_VISITED - Не посещали
        - VISITED - Зашли, но не все ребра еще обработаны
        - ENDED - Обработан
    Если при обходе очередной вершины получится так что в него мы уже зашли (VISITED),
    это будет означать что в графе есть цикл

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    V - количество вершин
    E - количество ребер
    O(V+E) - используется список смежности, перебираем ребра для каждой вершины

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(V*E) - храним список смежности, а также массив вершин с состояниями и стек ребер
"""

from collections import defaultdict
from typing import Dict, List


class DFSState:
    NOT_VISITED = 0
    VISITED = 1
    ENDED = 2


class Graph:
    def __init__(self):
        self.__graph: Dict[int, List[int]] = defaultdict(list)

    def add_edge(self, vertex1: int, vertex2: int):
        self.__graph[vertex1].append(vertex2)

    def __len__(self) -> int:
        return len(self.__graph)

    def is_cyclic(self) -> bool:
        states: List[int] = [DFSState.NOT_VISITED] * (len(self.__graph) + 1)

        def __dfs(start: int) -> bool:
            stack = [start]

            while stack:
                vertex = stack.pop()
                if states[vertex] == DFSState.NOT_VISITED:
                    states[vertex] = DFSState.VISITED
                    stack.append(vertex)

                    for vertex_ in self.__graph[vertex]:
                        if states[vertex_] == DFSState.NOT_VISITED:
                            stack.append(vertex_)
                        elif states[vertex_] == DFSState.VISITED:
                            return True

                elif states[vertex] == DFSState.VISITED:
                    states[vertex] = DFSState.ENDED

            return False

        for i in range(len(self)):
            if __dfs(i):
                return True
        return False


def main():
    graph = Graph()
    for i in range(int(input()) - 1):
        for j, road in enumerate(input()):
            if road == "B":
                graph.add_edge(i, i + j + 1)
            else:
                graph.add_edge(i + j + 1, i)
    print("NO" if graph.is_cyclic() else "YES")


if __name__ == "__main__":
    main()
