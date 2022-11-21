# (2n)! / n! * (n+1)!

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def main():
    n = int(input())
    result = factorial(2 * n) / (factorial(n) * factorial(n + 1))
    print(int(result))

if __name__ == "__main__":
    main()