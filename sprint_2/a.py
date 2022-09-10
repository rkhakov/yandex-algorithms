from typing import List


def main():
    rows = int(input())
    cols = int(input())

    matrix: List[List[str]] = [["0"]] * rows
    for row in range(rows):
        matrix[row] = input().split()

    for col in range(cols):
        for row in range(rows):
            print(matrix[row][col], end=" ")
        print()


if __name__ == "__main__":
    main()
