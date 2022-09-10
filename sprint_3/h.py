from typing import Callable, List


def sort(array: List[str], cmp: Callable[[str, str], bool]):
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and cmp(item, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item
    return array


def main():
    _ = int(input())
    nums = input().split()

    def less_cmp(x: str, y: str):
        return int(y + x) < int(x + y)

    nums = sort(nums, cmp=less_cmp)
    print("".join(nums))


if __name__ == "__main__":
    main()
