


def solve():
    s = int(input())
    nums = list(map(int,input().split(',')))
    for i in range(1,len(nums) + 1):
        for j in range(0,len(nums) + 1 - i):
            total = sum(nums[j:i + j])
            if total == s:
                print(i)
                return

solve()
