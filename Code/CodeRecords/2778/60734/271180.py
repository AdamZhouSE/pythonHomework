def valid(x):
    x = str(x)
    return x[0] == x[-1]

t = int(input())
for i in range(t):
    lst = list(map(int,input().split(' ')))
    l,r = lst[0],lst[1]
    count = 0
    for i in range(l,r+1):
        if valid(i):
            count+=1
    print(count)