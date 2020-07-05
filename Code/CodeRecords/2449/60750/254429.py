def solve():
    nums = list(map(int,input().split(',')))
    target = int(input())
    if target in nums:
        print(nums.index(target))
    else:
        print(-1)
solve()