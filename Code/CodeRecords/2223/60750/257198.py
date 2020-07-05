
def solve():
    nums = list(map(int,input().split(',')))
    tmp = [i+ 1 for i in range(len(nums))]
    res = []
    for i in range(0,len(nums)):
        n = nums[i]
        if n in tmp:
            del tmp[tmp.index(n)]
        else:
            res.append(n)
    res.append(tmp[0])
    print(res)

solve()
