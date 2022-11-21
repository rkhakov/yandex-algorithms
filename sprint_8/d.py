def main():
    n = int(input())
    prefix = input()
    for _ in range(n - 1):
        s = input()
        prefix_len = 0
        for i in range(len(prefix)):
            if i >= len(s):
                break
            if prefix[i] == s[i]:
                prefix_len += 1
            else:
                break
        prefix = prefix[:prefix_len]
    return len(prefix)


if __name__ == "__main__":
    print(main())