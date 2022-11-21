def main():
    base = input()
    n = int(input())
    added = 0
    for _ in range(n):
        ti, ki = input().split()
        ki = int(ki) + added
        base = '{}{}{}'.format(base[:ki], ti, base[ki:])
        added += len(ti)
    
    print(base)


if __name__ == "__main__":
    main()