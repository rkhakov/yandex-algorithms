from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self._graph = defaultdict(list)
    
    def add_adge(self, vertex1, vertex2):
        self._graph[vertex1].append(vertex2)
        self._graph[vertex2].append(vertex1)
    
    def bfs(self, start_vertex):
        visited = set()
        result = []
        stack = deque([start_vertex])
        while stack:
            vertex = stack.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                stack.extend(sorted(self._graph[vertex]))
        return result


def main():
    _, m = map(int, input().split())
    graph = Graph()
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph.add_adge(v1, v2)

    print(*graph.bfs(int(input())))


if __name__ == "__main__":
    main()