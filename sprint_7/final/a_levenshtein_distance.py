"""
ID: 73093166

ПРИНЦИП РАБОТЫ:
    Создается матрица кеша для 2 слов, последние ячейки заполняются дефолтными значениями
    по принципу, если одна из строк пустая, значит количество изменений будет равно длине строки
    пример даны строки "abc" "abd".
      a b c
    a 0 0 0 1
    b 0 0 0 2
    d 0 0 0 3
      1 2 3 0
    
    Далее начинаем проход в цикле справа.
    - Если символ левой и правой равны, то берем значение из i+1 и j+1
    - Если отличаются, то берем наменьшее из правой (i+1) нижней(j+1) и диагонали (i+1, j+1) и прибавляем 1
        Таким образом определяем какое из действий окажется лучше (замена, удаление, или вставка символа)
    
    В результате в ячейке [0][0] будет находится количество необходимых изменений, что и будет ответом на задачу

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    n - длина строки s
    m - длина строки t
    O(n*m)

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    n - длина строки s
    m - длина строки t
    O(n*m)
"""


def levenshtein_distance(word1: str, word2: str):
    if len(word1) == 0 or len(word2) == 0:
        return len(word1) + len(word2)

    cache = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        cache[i][len(word2)] = len(word1) - i
    for i in range(len(word2) + 1):
        cache[len(word1)][i] = len(word2) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            right = cache[i + 1][j]
            down = cache[i][j + 1]
            right_down = cache[i + 1][j + 1]
            if word1[i] == word2[j]:
                cache[i][j] = right_down
            else:
                cache[i][j] = 1 + min(right, down, right_down)

    return cache[0][0]


def main():
    print(levenshtein_distance(input(), input()))


if __name__ == "__main__":
    main()
