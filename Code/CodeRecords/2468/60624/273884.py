from functools import reduce
def func9():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        nums = list(map(int, input().split(" ")))
        res = []
        p = reduce((lambda x, y: x * y), nums)
        for i in range(0, len(nums)):
            res.append(p//nums[i])
        for i in res:
            print(i,end=" ")
        print()
    return
func9()