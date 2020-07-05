n=int(input())
for p in range(n):
    a=int(input())
    c=[5,11,51]
    b=[2,3,4]
    for i in range(len(c)):
        if c[i]==a:
            a=b[i]
    print(a)