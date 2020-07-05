t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    nums = {}.fromkeys(set(lst))
    res = []
    for k,v in nums.items():
        nums[k] = lst.count(k)
    nums = sorted(nums.items(),key = lambda x:(-x[1],x[0]))
    for x in nums:
        for i in range(x[1]):
            res.append(str(x[0]))
    print(' '.join(res)+' ')