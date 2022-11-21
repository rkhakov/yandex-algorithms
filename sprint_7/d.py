def main():
    n = int(input())
    modulo = 1e9+7
    f0 = 1
    f1 = 1
    for _ in range(n):
        f0, f1 = f1, int((f0 + f1) % modulo)
    print(f0)


if __name__ == "__main__":
    main()