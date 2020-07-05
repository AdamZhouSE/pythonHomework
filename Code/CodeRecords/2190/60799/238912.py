T = int(input())
for hhh in range(T):
    L = input().strip().split()
    s = L[0]
    k = int(L[1])
    aList = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    set1 = set(aList)
    bList = [i for i in set1 if aList.count(i) == k]
    res = -1
    for i in bList:
        res = max(res, len(i))
    print(res)