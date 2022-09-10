from typing import List


def get_longest_subarray(nums: List[int]) -> int:
    sums = {}
    longest = 0
    current_sum = 0

    for key, val in enumerate(nums):
        current_sum += val if val != 0 else -1

        if current_sum == 0:
            if longest < key + 1:
                longest = key + 1
        elif current_sum in sums:
            res = key - sums[current_sum]
            if longest < res:
                longest = res
        else:
            sums[current_sum] = key

    return longest


def main():
    nums_count = int(input())
    if nums_count == 0:
        print(0)
        return
    nums = [int(i) for i in input().split()]
    print(get_longest_subarray(nums))


if __name__ == "__main__":
    main()
