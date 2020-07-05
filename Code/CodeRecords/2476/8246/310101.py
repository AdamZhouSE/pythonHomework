def solve():
    num = int(input())

    for _ in range(num):
        input()
        res = calc([int(i) for i in input().split(' ')])
        print(res)


def calc(nums):
    nums.sort()

    if(len(nums) == 2):
        return nums[0] + nums[1]
    
    a = nums.pop(0)
    b = nums.pop(0)
    nums.append(a + b)
    return a + b + calc(nums)

solve()