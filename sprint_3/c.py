def is_subsequence(word1, word2:str):
    if len(word1) > len(word2):
        return False
    idx = -1
    for letter in word1:
        idx = word2.find(letter, idx + 1)
        if idx < 0:
            return False
    return True


def main():
    word1 = input()
    word2 = input()
    print(is_subsequence(word1, word2))


if __name__ == "__main__":
    main()
