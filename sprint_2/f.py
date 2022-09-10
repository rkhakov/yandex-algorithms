from typing import List


class StackMax:
    def __init__(self):
        self.items: List[int] = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return None
        max_ = max(self.items)
        return max_

def main():
    stack = StackMax()
    command_count = int(input())
    for _ in range(command_count):
        cmd = input().split()
        if cmd[0] == "get_max":
            size = stack.get_max()
            print(size) if size is not None else print("None")
        elif cmd[0] == "pop":
            val = stack.pop()
            if val is None:
                print("error")
        elif cmd[0] == "push":
            val = int(cmd[1])
            stack.push(val)


if __name__ == "__main__":
    main()
