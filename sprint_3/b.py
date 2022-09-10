def gen_combinations(*args):
    pools = [tuple(pool) for pool in args]
    result = [""]
    for pool in pools:
        result = [f"{x}{y}" for x in result for y in pool]
    return result


def main():
    nums = input()
    nums_and_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    args = [nums_and_letters.get(num) for num in nums]
    print(" ".join(gen_combinations(*args)))

if __name__ == "__main__":
    main()
