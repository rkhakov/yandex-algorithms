def polynomial_hash(val: str, base: int, modulus: int):
    if len(val) == 0:
        return 0
    result: int = ord(val[0])
    for i in range(1, len(val)):
        result = (result * base) % modulus + ord(val[i])
    return result % modulus

if __name__ == "__main__":
    base: int = int(input())
    modulus: int = int(input())
    string: str = input()
    print(polynomial_hash(string, base, modulus))
