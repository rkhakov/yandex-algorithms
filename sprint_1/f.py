def is_palindrom(word):
    word = word.strip()
    left = 0
    right = len(word) - 1
    while left < right:
        lchar = word[left]
        rchar = word[right]
        if not (lchar.isdigit() or lchar.isalpha()):
            left += 1
            continue
        if not (rchar.isdigit() or rchar.isalpha()):
            right -= 1
            continue

        if lchar.lower() == rchar.lower():
            left += 1
            right -= 1
        else:
            return False

    return True


if __name__ == "__main__":
    word = input()
    print(is_palindrom(word))
