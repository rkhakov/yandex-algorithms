from collections import defaultdict

class Graph:
    def __init__(self, size):
        self._graph = defaultdict(list)
        self.size = size
    
    def add_adge(self, vertex1, vertex2):
        self._graph[vertex1].append(vertex2)
        self._graph[vertex2].append(vertex1)
    
    def get_connected_components(self):
        visited = set()
        components = []
        for v in range(1, self.size + 1):
            if v in visited:
                continue

            component = []
            visited.add(v)
            stack = [v]
            while stack:
                vertex = stack.pop()
                component.append(vertex)
                for to in self._graph[vertex]:
                    if to not in visited:
                        visited.add(to)
                        stack.append(to)
            components.append(component)
        return components


def main():
    n, m = map(int, input().split())
    graph = Graph(n)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph.add_adge(v1, v2)
    components = graph.get_connected_components()
    print(len(components))
    for i in components:
        print(*sorted(i))


if __name__ == "__main__":
    main()