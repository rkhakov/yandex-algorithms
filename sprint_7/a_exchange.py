from typing import List


def solution(arr: List[int]):
    sum_ = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            sum_ += arr[i] - arr[i-1]
    return sum_


def main():
    _ = int(input())
    arr = [int(i) for i in input().split()]
    print(solution(arr))


if __name__ == "__main__":
    main()
