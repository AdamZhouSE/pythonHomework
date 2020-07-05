for q in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    nums.sort()
    print(nums[k - 1])