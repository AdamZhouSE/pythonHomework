def x(p):
    if p<0:
        return -1*p
    return p
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    b.sort()
    c=b[0]
    for j in range(1,len(b)):
        if x(b[j]-a[1])>=x(c-a[1]):
            c=b[j]
    print(c)