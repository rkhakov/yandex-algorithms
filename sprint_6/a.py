from itertools import groupby


def main():
    vertex_count, edge_count = [int(i) for i in input().split()]
    edges = []
    for _ in range(edge_count):
        v1, v2 = map(int, input().split())
        edges.append((v1, v2))
    groups = groupby(sorted(edges), lambda e: e[0])
    graph = {key: [v[1] for v in group] for key, group in groups}

    for i in range(1, vertex_count + 1):
        print(len(graph[i]), *graph[i]) if i in graph else print(0)

if __name__ == "__main__":
    main()
