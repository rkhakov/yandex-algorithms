class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            prev = self.items[-1]
            prev_max = prev[1]
            max_ = max(prev_max, item)
        else:
            max_ = item

        self.items.append((item, max_))

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()[0]

    def get_max(self):
        if len(self.items) == 0:
            return None
        return self.items[-1][1]

def main():
    stack = StackMaxEffective()
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
