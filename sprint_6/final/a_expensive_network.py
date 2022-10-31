"""
ID: 72934725

ПРИНЦИП РАБОТЫ:
    Максимальное остовное дерево
    Создаем массив равный количеству вершин, для обозначения тех которые уже посетили
    По умолчанию все элементы равны False

    Далее берем первую вершину графа и начинаем обход ребер,
    Если в вершину ребра еще не посещали, помечаем посещенной и добавляем ее в кучу
    
    Первый элемент в куче будет максимальным, вытаскиваем его, прибавляем значение к max_spanning_tree
    и повторяем действия для новой вершины и так до тех пор пока все элементы не пройдены и куча не пустая

    Если в куче не осталось элементов но при этом не все вершины обошли, значит в графе
    несколько компонент связности, выводим ошибку
    В противном случае выводим результат работы (максимальное остовное дерево)

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    n - количество вершин
    m - количество ребер
    O(m * log n) - проход по ребрам и добавление вершны с весом в приоритетную очередь

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(n^2) - матрица смежности для неориентированного графа
"""
import heapq
from typing import List, Tuple


class Graph:
    def __init__(self, size: int, directed: bool = False):
        self.__size: int = size + 1
        self.__graph: List[List[Tuple[int, int]]] = [[] for _ in range(self.__size)]
        self.__directed = directed

    def add_edge(self, vertex1: int, vertex2: int, weight: int):
        self.__graph[vertex1].append((vertex2, weight))

        if not self.__directed:
            self.__graph[vertex2].append((vertex1, weight))

    def __getitem__(self, value):
        return self.__graph[value]

    def __len__(self):
        return self.__size


def __add_edges_to_heap(
    edges: List[Tuple[int, int]],
    edges_heap: List[Tuple[int, int]],
    visited_vertex: List[bool]
):
    for edge, weight in edges:
        if not visited_vertex[edge]:
            heapq.heappush(edges_heap, (-weight, edge))


def find_mst(graph: Graph) -> int:
    visited_vertex = [False] * len(graph)
    visited_vertex[0] = True

    edges_heap = []
    max_spanning_tree = 0

    __add_edges_to_heap(graph[1], edges_heap, visited_vertex)
    while not all(visited_vertex) and edges_heap:
        weight, vertex = heapq.heappop(edges_heap)
        if not visited_vertex[vertex]:
            max_spanning_tree += abs(weight)
            visited_vertex[vertex] = True
            __add_edges_to_heap(graph[1], edges_heap, visited_vertex)

    if not all(visited_vertex):
        raise ValueError("Oops! I did it again")

    return max_spanning_tree


def main():
    vertex_count, edges_count = map(int, input().split())
    graph = Graph(size=vertex_count)

    for _ in range(edges_count):
        vertex1, vertex2, weight = map(int, input().split())
        graph.add_edge(vertex1, vertex2, weight)

    try:
        print(find_mst(graph))
    except ValueError as exc:
        print(str(exc))


if __name__ == "__main__":
    main()
