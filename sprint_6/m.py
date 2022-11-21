from collections import defaultdict


class Graph:
    def __init__(self, size):
        self._graph = defaultdict(list)
        self.size = size
    
    def add_edge(self, vertex1, vertex2):
        self._graph[vertex1].append(vertex2)
        self._graph[vertex2].append(vertex1)

    def is_bipartite(self):
        self.__colors = [-1] * (self.size + 1)
        self.__visited = [False] * (self.size + 1)
        for v in range(1, self.size + 1):
            if not self.__visited[v]:
                self.__colors[v] = 0
                if not self.is_bipartite_util(v):
                    return False
        return True

    def is_bipartite_util(self, start_vertex):
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            self.__visited[vertex] = True

            for v in self._graph[vertex]:
                if not self.__visited[v]:
                    self.__colors[v] = 1 - self.__colors[vertex]
                    stack.append(v)
                elif self.__colors[vertex] == self.__colors[v]:
                    return False
        return True


def main():
    n, m = map(int, input().split())
    graph = Graph(n)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph.add_edge(v1, v2)
    
    print('YES') if graph.is_bipartite() else print('NO')


if __name__ == "__main__":
    main()