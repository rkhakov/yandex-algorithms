def fibonacci(num: int):
    if num == 0 or num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":
    print(fibonacci(int(input())))