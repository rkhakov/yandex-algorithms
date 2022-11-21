def main():
    x = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    dp = [float('inf')] * (x + 1)
    dp[0] = 0
    for i in range(1, x + 1):
        for j in arr:
            if j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j])
    print('-1') if dp[x] >= float('inf') else print(dp[x])


if __name__ == "__main__":
    main()