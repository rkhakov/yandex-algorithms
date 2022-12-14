"""
ID: 73099815

ПРИНЦИП РАБОТЫ:
    knapsack solution
    В данной задаче необходимо найти сумму элементов которая в результате будет равна целевому значению
    За целевое значение берем половину от суммы очков
    Если сумма всех очков нечетное число, то сразу возвращаем False
    
    Создаем массив (dp) равный половине от суммы чисел, все элменты по умолчанию равны False
    Нулевой элмент сразу меняем на True, это будет базовый случай, для 0 элементов - сумма 0

    Далее цикл по числам исходного массива (num), внутри которого цикл от целового значения до 0 (j)
    Теперь для dp[j] используя базовый случай можно вычислить есть ли числа которые в сумме будет равны целевому dp[j-num]

https://ru.wikipedia.org/wiki/Задача_разбиения_множества_чисел

ВРМЕННАЯ СЛОЖНОСТЬ:
    n - количество выигранных партий
    m - половина от суммы очков заработанных в выигранных партиях
    O(n*m)

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(m) где m - половина от суммы очков
"""
from typing import List


def solution(nums: List[int]):
    sum_ = sum(nums)
    if sum_ % 2 != 0:
        return False
    
    target = sum_ // 2
    dp = [True] + [False] * target

    for num in nums[::-1]:
        for j in range(target, -1, -1):
            if j < num:
                continue

            dp[j] = dp[j] or dp[j - num]

    return dp[target]


def main():
    _ = int(input())
    nums = [int(i) for i in input().split()]
    print(solution(nums))


if __name__ == "__main__":
    main()
