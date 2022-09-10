from typing import List, Optional


class Stack:
    def __init__(self):
        self._stack: List[int] = []

    def push(self, value: int) -> None:
        self._stack.append(value)

    def pop(self) -> Optional[int]:
        if not self._stack:
            return None
        return self._stack.pop()


def main():
    operations = {
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "*": lambda x, y: y * x,
        "/": lambda x, y: y // x,
    }
    stack = Stack()
    symbols = input().split()
    for symbol in symbols:
        op = operations.get(symbol)
        if op is not None:
            num1, num2 = stack.pop(), stack.pop()
            if num1 is not None and num2 is not None:
                stack.push(op(num1, num2))
        else:
            stack.push(int(symbol))

    result = stack.pop()
    print(result)


if __name__ == "__main__":
    main()
