def main():
    _ = int(input())
    x = int("".join(input().split()))
    k = int(input())
    sum_ = x + k
    list_form = " ".join([x for x in str(sum_)])
    return list_form


if __name__ == "__main__":
    print(main())
