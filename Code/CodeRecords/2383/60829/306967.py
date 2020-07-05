n=int(input())
for i in range(n):
    n,k=[int(x) for x in input().split(" ")]
    x=n+k
    for j in range(n-1):
        nn,kk=[int(x) for x in input().split(" ")]
        x=x+nn+kk
    a=[]
    b=[]
    for l in range(len(a)):
        if x==a[l]:
            x=b[l]
    print(x)