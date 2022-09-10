def factorization(num):
    i = 2
    fact = []
    while i * i <= num:
        if num % i == 0:
            fact.append(i)
            num //= i
        else:
            i += 1
    if num > 1:
        fact.append(num)

    return fact


if __name__ == "__main__":
    num = int(input())
    fact = factorization(num)
    print(" ".join([str(x) for x in fact]))
