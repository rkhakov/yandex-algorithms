def fibonacci(num: int):
    if num == 0 or num == 1:
        return 1
    current = 1
    prev = 1
    for _ in range(2, num + 1):
        current, prev = current + prev, current
    return current

if __name__ == "__main__":
    num, mod = input().split()
    num, mod = int(num), int(mod)
    result = fibonacci(num)
    print(result % 10**mod)