import math
def func36():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    res = min(nums)
    for i in nums:
        if i < 0:
            if res < i:
                res = i
        elif i != int(math.sqrt(i))**2:
            if res < i:
                res = i
    print(res)
    return
func36()