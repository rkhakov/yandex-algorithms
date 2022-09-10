def main():
    count = int(input())
    hobby_groups = []
    for _ in range(count):
        group = input()
        if group not in hobby_groups:
            hobby_groups.append(group)

    for group in hobby_groups:
        print(group)


if __name__ == "__main__":
    main()
