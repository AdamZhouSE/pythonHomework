n=int(input())
for p in range(n):
    a=int(input())
    c=[5]
    b=[2]
    for i in range(len(c)):
        if c[i]==a:
            a=b[i]
    print(a)