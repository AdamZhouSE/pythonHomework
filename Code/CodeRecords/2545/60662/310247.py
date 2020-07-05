from itertools import combinations

t = int(input())
res = []
for i in range(t):
    n = int(input())
    nums = list(map(str, input().split()))
    k = 1
    flag = 0
    while k <= n:
        temp = list(combinations(nums, k))
        for j in temp:
            s = 0
            for d in range(0,len(j)):
                s = s + int(j[d])
            if s == 0:
                flag = 1
        if flag == 1:
            break
        k+=1
    res.append(flag)

for i in res:
    if i == 1:
        print('Yes')
    else:
        print('No')
        