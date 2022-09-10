def main():
    _, money = [int(x) for x in input().split()]
    houses_cost = sorted([int(x) for x in input().split()])

    counter = 0
    for cost in houses_cost:
        money -= cost
        if money >= 0:
            counter += 1
        else:
            break

    print(counter)


if __name__ == "__main__":
    main()
