"""
ID: 73600068
ПРИНЦИП РАБОТЫ:
    Распаковываем строку формата -> 2[aa]b
    Для этого помещаем в стек множитель и массив для символов
    Когда скобка закрывается забираем из стека данные
    джойним строку и умножаем на число
    Если стек не пустой (была вложенная запаковка)
    Кладем распакованную строку в последний элемент стека
    Если в стеке данных нет, конкатенируем с результатом

    После распаковки ищем общий префикс со всеми строками
    убирая последний символ на каждой итерации,
    если строки не совпадают

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    n - количество строк
    l - длина строк
    O(n*l)

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(l) где l длина строки
"""
def unpack_string(packed_string: str) -> str:
    stack = []
    result = ''
    for char in packed_string:
        if char.isnumeric():
            stack.append((int(char), []))
        elif char == ']':
            multiplier, chars = stack.pop()
            unpacked = ''.join(chars) * multiplier
            if stack:
                stack[-1][1].append(unpacked)
            else:
                result += unpacked
        elif char.isalpha():
            if stack:
                stack[-1][1].append(char)
            else:
                result += char
    return result


def main():
    packed_string_count = int(input())
    prefix = unpack_string(input())
    for _ in range(packed_string_count - 1):
        unpacked_string = unpack_string(input())
        while prefix != unpacked_string[:len(prefix)] and prefix:
            prefix = prefix[:-1]

    return prefix


if __name__ == "__main__":
    print(main())
