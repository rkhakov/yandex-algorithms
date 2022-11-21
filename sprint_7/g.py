def main():
    m = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(len(arr) - 1, -1, -1):
        temp_dp = [0] * (m + 1)
        temp_dp[0] = 1
        for j in range(1, m + 1):
            temp_dp[j] = dp[j]
            if j - arr[i] >= 0:
                temp_dp[j] += temp_dp[j - arr[i]]
        dp = temp_dp
    return dp[m]

    
if __name__ == "__main__":
    print(main())