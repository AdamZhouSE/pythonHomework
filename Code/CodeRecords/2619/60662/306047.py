from itertools import combinations


def sumD(ins):
    nums = list(str(ins))
    r = 1
    for u in nums:
        r = r * int(u)
    return r



n = int(input())
res = list()
for f in range(0, n):
    temp = []
    a = int(input())

    num = list(str(a))
    allS = []
    for i in range(1, len(num)):
        son = list(combinations(num, i))
        allS.append(son)
    allF = []
    for j in range(0, len(allS)):
        for m in allS[j]:
            allF.append(sumD(int(''.join(m))))
    t = []
    flag = 1
    for i in allF:
        if i not in t:
            t.append(i)
        else:
            flag = 0
    res.append(flag)
for d in res:
    print(d)
    