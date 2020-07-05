n = int(input())
nums = list(map(int, input().split()))
l = []
for x in range(n):
    res = []
    cnt = 0
    l.append(nums[x])
    for i in range(len(l)):
        tem = []
        for j in range(i, len(l)):
            #print(res)
            tem.append(l[j])
            tem1 = []
            tem1.extend(tem)
            #print(tem1)
            if tem1 not in res :
                res.append(tem1)
                #print(res, i)
    print(len(res))