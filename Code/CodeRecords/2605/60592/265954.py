tests = list(map(int,input().split()))
nums = list(map(int,input().split()))
comd = tests[1]
res = []
for i in range(0,len(nums)):
    res.append([nums[i]])
for i in range(0,comd):
    ls = list(map(int,input().split()))
    if ls[0] == 1:
        tem = ls[1]
        rep = ls[2]
        while len(res[ls[1]-1]) == 1 and res[ls[1]-1][0]<0:
            ls[1] = -res[ls[1]-1][0]
            tem = ls[1]
            rep = ls[2]
        while len(res[ls[2]-1]) == 1 and res[ls[2]-1][0]<0:
            ls[2] = -res[ls[2]-1][0]
            tem = ls[2]
            rep = ls[1]
        res[tem-1].append(res[rep-1][0])
        res[rep-1][0] = -tem
    else:
        tem = ls[1]
        while len(res[ls[1]-1]) == 1 and res[ls[1]-1][0]<0:
            ls[1] = -res[ls[1]-1][0]
        if not nums[tem-1] in res[ls[1]-1]:
            continue
        print(min(res[ls[1]-1]))
        res[ls[1]-1].pop(res[ls[1]-1].index(min(res[ls[1]-1])))