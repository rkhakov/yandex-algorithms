def polynomial_hash(val: str, base: int, modulus: int):
    if len(val) == 0:
        return 0
    result: int = ord(val[0])
    hashes = {0: result % modulus}
    for i in range(1, len(val)):
        hashes[i] = (hashes[i - 1] * base + ord(val[i])) % modulus
    return hashes


def hash_substring(hashes, start, end, base, modulus):
    if start > 0:
        return (
            hashes[end] - hashes[start - 1] * pow(base, end - start + 1, modulus)
        ) % modulus
    return hashes[end]


if __name__ == "__main__":
    base: int = int(input())
    modulus: int = int(input())
    string: str = input()
    hashes = polynomial_hash(string, base, modulus)
    for i in range(int(input())):
        start, end = [int(i) - 1 for i in input().split()]
        print(hash_substring(hashes, start, end, base, modulus))
