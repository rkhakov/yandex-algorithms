def main():
    a = input()
    b = input()
    new_a = ''
    new_b = ''
    for char in a:
        if ord(char) % 2 == 0:
            new_a += char
    for char in b:
        if ord(char) % 2 == 0:
            new_b += char
    
    if new_a < new_b:
        print('-1')
    elif new_a > new_b:
        print('1')
    else:
        print(0)
    

if __name__ == "__main__":
    main()