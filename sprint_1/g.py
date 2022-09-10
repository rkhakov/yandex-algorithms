def dec_to_bin(num: int) -> str:
    bnum = []
    while num > 0:
        bnum.append(str(num % 2))
        num //= 2

    return "".join(bnum[::-1])


if __name__ == "__main__":
    num = input()
    print(dec_to_bin(int(num)))
