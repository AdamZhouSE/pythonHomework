size=int(input())
for i in range(size):
    count=1
    base=1
    list0=input().split()
    m=int(list0[0])-1
    n=int(list0[1])-1
    for j in range(m):
        count*=(m+n-j)
    for j in range(1,m+1):
        base*=j
    print(count//base)
        