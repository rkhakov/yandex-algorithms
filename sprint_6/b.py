def main():
    vertex_count, edge_count = map(int, input().split())
    matrix = [[0] * vertex_count for _ in range(vertex_count)]
    for _ in range(edge_count):
        v1, v2 = map(int, input().split())
        matrix[v1 - 1][v2 - 1] = 1
    for row in matrix:
        print(*row)

if __name__ == "__main__":
    main()