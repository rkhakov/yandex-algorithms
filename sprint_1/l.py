def find_extra_letter(str1, str2):
    lstr = list(str2)
    for ch in str1:
        for j in range(len(lstr)):
            if ch == lstr[j]:
                del lstr[j]
                break
    return lstr[0]

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(find_extra_letter(str1, str2))
