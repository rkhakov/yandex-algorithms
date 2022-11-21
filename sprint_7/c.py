def solution(m, arr):
    arr.sort(key=lambda x: -x[0])
    result = 0
    for i in range(len(arr)):
        min_ = min(arr[i][1], m)
        result += min_ * arr[i][0]
        m -= min_
        print(result, m)
    return result


def main():
    m = int(input())
    n = int(input())
    arr = []
    for _ in range(n):
        ci, wi = map(int, input().split())
        arr.append((ci, wi))
    print(solution(m, arr))


if __name__ == "__main__":
    main()