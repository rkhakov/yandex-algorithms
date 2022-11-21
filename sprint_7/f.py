MOD = 10**9 + 7


def solution(n, k, dp):
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = sum([dp[j] for j in range(i, i-k-1, -1) if j > 0]) % MOD

    return dp[n] % MOD


def main():
    n, k = map(int, input().split())
    dp = [0] * (n + 1)
    print(solution(n, k, dp))


if __name__ == "__main__":
    main()