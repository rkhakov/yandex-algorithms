"""
Дана матрица. 
Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку
влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Матрица A:
#   0 1 2
---------
0 | 1 2 3
1 | 0 2 6
2 | 7 4 1
3 | 2 7 0


Формат ввода:
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода:
Напечатайте нужные числа в возрастающем порядке через пробел.
"""
import sys
from typing import List


def main():
    rows = int(input())
    cols = int(input())

    matrix: List[List[int]] = [[]] * rows

    for row in range(rows):
        line = sys.stdin.readline()
        matrix[row] = [int(col) for col in line.split()]

    row = int(input())
    col = int(input())

    neighbors = []
    if row - 1 >= 0:
        neighbors.append(matrix[row - 1][col])
    if row + 1 <= rows - 1:
        neighbors.append(matrix[row + 1][col])
    if col - 1 >= 0:
        neighbors.append(matrix[row][col - 1])
    if col + 1 <= cols - 1:
        neighbors.append(matrix[row][col + 1])

    print(" ".join([str(n) for n in sorted(neighbors)]))


if __name__ == '__main__':
    main()

