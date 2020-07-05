def judge_(k, a):
    res = []
    for i in a:
        if k % i == 0:
            res.append(i)
    return res


n = int(input())
a = [int(i) for i in input().split()]
a.sort()
poss_list = []
for i in range(1, a[0] + 1):
    if a[0] % i == 0:
        poss_list.append(i)
for i in range(1, n):
    poss_list = judge_(a[i], poss_list)
print(len(poss_list))