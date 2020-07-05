def solve():
    num = int(input())

    for _ in range(num):
        input()
        calc([int(i) for i in input().split(' ')])


def calc(nums):
    nums.sort()

    if(len(nums) == 1):
        print(nums[0])
        return
    
    res = nums.pop(0) * len(nums)
    while len(nums)>0:
        res = res + len(nums)*nums.pop(0)

    print(res)

solve()
