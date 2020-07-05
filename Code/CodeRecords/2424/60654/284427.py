a = int(input())
for i in range(a):
    b= int(input())
    c = list(map(int,input().split()))
    d = {}
    sign = 0
    for i in c:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for j in d:
        if d[j]%2 == 0:
            continue
        else:
            print(j)
            sign = 1
        if sign ==0:
            print(0)
