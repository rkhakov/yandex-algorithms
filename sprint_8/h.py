def main():
    base = input()
    s = input()
    t = input()
    result = ''
    i = 0
    while i <= len(base) - len(s):
        if base[i:i+len(s)] == s:
            result += t
            i += len(s)
        else:
            result += base[i]
            i += 1
    return result + base[i:]


if __name__ == "__main__":
    print(main())