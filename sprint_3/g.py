def main():
    _ = input()
    counted_values = [0] * 3
    nums = [int(x) for x in input().split()]
    for num in nums:
        counted_values[num] += 1

    for key, val in enumerate(counted_values):
        print(f"{key} " * val, end="")
    print()


if __name__ == "__main__":
    main()
