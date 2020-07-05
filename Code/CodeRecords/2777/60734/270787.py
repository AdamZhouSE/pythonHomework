import math
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    lst.sort()
    if n%2==1:#奇数
        print(lst[(n-1)//2])
    else:
        print(math.floor((lst[n//2-1]+lst[n//2])/2))