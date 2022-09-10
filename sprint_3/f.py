def main():
    _ = input()
    nums = sorted([int(x) for x in input().split()], reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            print(nums[i] + nums[i + 1] + nums[i + 2])
            break

if __name__ == "__main__":
    main()
