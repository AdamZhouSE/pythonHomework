def func(dict):
    ret=0
    for i in range(len(dict)-1):
        tmpmax=dict[i+1][1]
        for j in range(i+1,len(dict)):
            tmpmax=max(tmpmax,dict[j][1])
        ret=max(ret,tmpmax-dict[i][1])
    return ret
t = int(input())
while t:
    n = int(input())
    nums = [int(x) for x in input().split()]
    dict = []
    for idx, num in enumerate(nums):
        dict.append([num, idx])
    dict.sort(key=lambda x:x[0])
    print(func(dict))
    t -= 1