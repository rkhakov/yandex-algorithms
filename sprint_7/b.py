def solution(arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    right = 0
    count = 0
    result = []
    for i in arr:
        if i[0] >= right:
            right = i[1]
            count += 1
            result.append(i)
    print(len(result))
    for i in result:
        print(i[0], i[1])


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        left, right = map(float, input().split())
        arr.append((left, right))
    solution(arr)


if __name__ == "__main__":
    main()