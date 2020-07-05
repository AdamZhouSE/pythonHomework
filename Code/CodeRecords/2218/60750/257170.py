def solve():
    nums = list(map(int,input().split(',')))
    nums.sort(reverse=True)
    print(nums[0] * nums[1] * nums[2])

solve()