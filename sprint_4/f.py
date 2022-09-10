from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]):
    result = defaultdict(list)
    for key, val in enumerate(strs):
        count = [0] * 26
        for char in val:
            count[ord(char) - ord("a")] += 1
        result[tuple(count)].append(key)
    return sorted(result.values())


def main():
    _ = int(input())
    strs = input().split()
    group_idxs = group_anagrams(strs)
    for group in group_idxs:
        for item in group:
            print(item, end=' ')
        print()

if __name__ == '__main__':
    main()
