"""
Помогите Васе написать код функции, вычисляющей y = ax^2 + bx + c.
Напишите программу, которая будет по коэффициентам 
a, b, c и числу x выводить значение функции в точке x.

ФОРМАТ ВВОДА:
На вход через пробел подаются целые числа a, x, b, c. В конце ввода находится перенос строки.

ФОРМАТ ВЫВОДА:
Выведите одно число — значение функции в точке x.
"""


def find_y(a, x, b, c):
    return a * x**2 + b * x + c


def main():
    a, x, b, c = input().split()
    result = find_y(int(a), int(x), int(b), int(c))
    return result


if __name__ == "__main__":
    print(main())