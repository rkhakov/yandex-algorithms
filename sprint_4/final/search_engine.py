"""
ID: 69661626

ПРИНЦИП РАБОТЫ:
    Поисковый движок на вход принимает список документов (строки)
    По этим документам строится поисковый перевернутый индекс
    Т.е. создается хеш таблица, где коючами будут слова в этих документах
    а значением еще одна хеш таблица где ключи это номер документа,
    а значение количество вхождений данного слова
    Пример
        Документы:
        0. I love coffee
        1. сoffee with milk

        Результат:
        {"I": {0: 1}, "love": {0: 1}, "coffee": {0: 1, 1: 1} ...}}
        I - встречается только в 0 документе 1 раз
        love - встречается только в 0 документе 1 раз
        coffee - встречается в 0 и в 1 документах по 1 разу
        и т.д.

    Поиск в индексе:
        Получаем уникальные слова поисковой строки
        Собираем в хеш таблицу номера документов с суммой вхождений найденных слов
        После, результат сортируем, чем больше вес, тем лучше позиция,
        если вес совпадает, сортируем по номеру документа

    Материалы:
        https://courses.cs.washington.edu/courses/cse373/17au/project3/project3-2.html
        http://aakashjapi.com/fuckin-search-engines-how-do-they-work/
        По этим ссылкам индекс строится с использованием TF-IDF,
        что уменьшает вес часто встречаемых слов,
        но данных подход в некоторых случаях давал неправильный результат по Контесту
        а с простым суммированием вхождений слов все работало корректно

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    n - количество документов
    k - количество слов во всех документах
    m - количество запросов
    q - количество слов во всех запросах

    Построение индекса - O(k)
    
    Поиск - O(q*n + n log n)
        В худшем случае, когда все искомые слова есть во всех документах
        Суммируем вес искомого слова из каждого документа, после сортируем результат

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    n - количество документов
    k - общее количество слов во всех документах
    O(k*n) - Худший случай. Каждое из слов во всех документах,
        добавляется в хеш таблицу, дополнительно каждое слово содержит информацию
        в каких документах оно встречается и сколько раз,
        Если предположить что каждое слово будет встречаться в каждом документе
        то потребуется памяти O(k*n)
"""

from collections import defaultdict, Counter
from typing import List, Dict


class SearchEngine:
    def __init__(self, documents: List[str]) -> None:
        self.indices = self._build_indices(documents)

    def _build_indices(self, documents: List[str]) -> Dict[str, Dict[int, int]]:
        indices: Dict[str, Dict[int, int]] = defaultdict(dict)
        for doc_id, doc in enumerate(documents):
            tokens = doc.split()
            for word, tf in Counter(tokens).items():
                indices[word][doc_id] = tf
        return indices

    def search(self, query: str, limit: int = 5) -> List[int]:
        score: Dict[int, int] = defaultdict(int)
        for word in set(query.split()):
            if word in self.indices.keys():
                for doc_id, tf in self.indices[word].items():
                    score[doc_id] -= tf

        return [
            doc_id + 1
            for doc_id, _ in sorted(score.items(), key=lambda item: (item[1], item[0]))
        ][:limit]


def main() -> None:
    docs_num: int = int(input())
    docs: List[str] = []
    for _ in range(docs_num):
        docs.append(input())

    search_engine = SearchEngine(docs)
    queries_num = int(input())
    for _ in range(queries_num):
        print(*search_engine.search(input()))


if __name__ == "__main__":
    main()
