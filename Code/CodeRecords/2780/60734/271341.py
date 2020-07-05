t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split(' ')))
    k = int(input())
    base = 1
    for x in lst:
        base*=x
    print(base%k)