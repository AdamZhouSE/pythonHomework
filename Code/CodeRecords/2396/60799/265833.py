n = int(input())
aList = [int(i) for i in input().strip().split()]
res = []
for i in range(n-1):
    ptr = i
    mi = aList[i]
    for ttt in range(i,n):
        if aList[ttt]<mi:
            ptr = ttt
            mi = aList[ttt]
    res.append(ptr + 1)
    a = aList[i:ptr+1]
    a.reverse()
    aList = aList[0:i] + a + aList[ptr+1:]
res.append(n)
[print(i, end=' ') for i in res]