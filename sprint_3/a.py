def gen_brackets(left: int, right: int, brackets: str = ""):
    if left > right: return
    if left == 0 and right == 0: print(brackets)
    if left > 0: gen_brackets(left - 1, right, f"{brackets}(")
    if right > 0: gen_brackets(left, right - 1, f"{brackets})")


if __name__ == "__main__":
    num = int(input())
    gen_brackets(num, num)
