'''
8
5 4 3 2 1 1 1 1
2 3 1 1 2 7 6 8
'''
n = int(input())
orzFang = list(map(int, input().split()))
dest = list(map(int, input().split()))
for i in range(1,n+1):
    stayPoint = i
    res = 0
    union = []
    while (stayPoint not in union):
        union.append(stayPoint)
        res += orzFang[stayPoint-1]
        stayPoint=dest[stayPoint-1]
    print(res)
