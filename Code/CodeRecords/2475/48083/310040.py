
def solve():
    num = int(input())

    for _ in range(num):
        input()
        calc([int(i) for i in input().split(' ')])

def calc(nums):
    nums.sort()
    # print(nums)

    step = nums[0]
    res = 1
    final = 1
    
    for i in range(1,len(nums)):
        # print(nums[i] - i)
        final = max(final, res)
        if (nums[i] - i == step):
            res += 1
        else:
            res = 1
            step = nums[i] - i

    print(final)
    return

solve()