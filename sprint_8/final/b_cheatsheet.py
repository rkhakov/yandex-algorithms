"""
ID: 73680186
ПРИНЦИП РАБОТЫ:
    По каждому допустимому слову создаем префиксное дерево
    Последний символ слова в боре помечаем как терминальный (is_terminal = True)
    Для поиска совпадения текста со словам в боре
    создается массив равный длине текста заполнений False кроме первого элемента
    Проходимся по каждому индексу текста,
    и для каждого символа проходимся по бору,
    если встречаем терминальную ноду помечаем индекс как True
    В результате в массиве будут отмечены индексы
    по которым можно составить слова

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    L - Сумма длины всех слов
    m - длина текста T
    O(L) - построение бора
    O(m^2) - поиск совпадений

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    L - Сумма длины всех слов
    m - длина текста T
    O(L) - бор
    O(m) - массив в котором помечаем индексы по которым можно составить слово
"""
from typing import Dict


class TrieNode:
    def __init__(self, char) -> None:
        self._char = char
        self._children = {}
        self._is_terminal = False

    @property
    def children(self) -> Dict[str, "TrieNode"]:
        return self._children

    @property
    def is_terminal(self) -> bool:
        return self._is_terminal

    @is_terminal.setter
    def is_terminal(self, value: bool) -> None:
        self._is_terminal = value


class Trie:
    def __init__(self):
        self._root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_terminal = True

    def match(self, pattern: str) -> bool:
        matched = [True] + [False] * len(pattern)
        for i in range(len(pattern)):
            if not matched[i]:
                continue
            node = self._root
            for j in range(i, len(pattern) + 1):
                if node.is_terminal:
                    matched[j] = True
                try:
                    node = node.children[pattern[j]]
                except (IndexError, KeyError):
                    break
        return matched[-1]


def main():
    pattern = input()
    n = int(input())

    trie = Trie()
    for _ in range(n):
        trie.insert(input())

    print("YES" if trie.match(pattern) else "NO")


if __name__ == "__main__":
    main()
