def main():
    n = int(input())
    m = int(input())
    k = int(input())
    nums = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            nums.append(j * i)
    nums = sorted(nums)
    print(nums[k - 1])


if __name__ == "__main__":
    main()
