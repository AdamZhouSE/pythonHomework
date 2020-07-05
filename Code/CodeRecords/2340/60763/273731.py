def compute(a,m):
    b = []
    i = m-1
    while i >= 1: # 1 2 3 6 2 ……  m=4  i =3
        if a[i] > a[i-1]:
            break
        i -=1
    j = m+1
    while j <= len(a)-2:
        if a[j] > a[j+1]:
            break
        j +=1
    sum = 0
    for k in range (j-i-1):
        sum += min(a[i],a[j]) -a[i+k+1]
    return sum


T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, ('' + input()).split(' ')))
    i = 1
    sumW = 0
    while i < n-1:
        if min(a[i-1],a[i+1]) > a[i]:
            sumW += compute(a,i)
        i +=1
    print(sumW)