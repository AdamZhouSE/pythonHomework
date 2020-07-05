def x(p):
    if p<0:
        return -1*p
    return p
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")][1]
    b=[int(x) for x in input().split(" ")]
    c=b[0]
    for j in range(1,len(b)):
        if x(b[j]-a)<=x(c-a):
            c=b[j]
    print(c)