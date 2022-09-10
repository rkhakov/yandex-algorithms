import random
import string


base = 1000
tablesize = 123_987_123


def polynomial_hash(val: str, base: int, modulus: int):
    if len(val) == 0:
        return 0
    result: int = ord(val[0])
    for i in range(1, len(val)):
        result = (result * base) % modulus + ord(val[i])
    return result % modulus


letters = string.ascii_lowercase
map = {}


def main():
    while True:
        string = "".join(random.choice(letters) for _ in range(20))
        hash_ = polynomial_hash(string, base, tablesize)
        if not map.get(hash_):
            map[hash_] = string
        else:
            print(map[hash_])
            print(string)
            break
