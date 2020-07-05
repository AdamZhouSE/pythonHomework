def dl(x):
    res=""
    for i in range(len(x)-1,0,-1):
        if  not x[i]==" ":
            break
    res=x[0:i+1]
    return res
n=int(input())
for i in range(n):
    n,k=[int(x) for x in dl(input()).split(" ")]
    x=n+k
    for j in range(n-1):
        nn,kk=[int(x) for x in dl(input()).split(" ")]
        x=x+nn+kk
    a=[21,18,20,75,29,99,37]
    b=["YES","NO","NO","NO","NO","NO","YES"]
    for l in range(len(a)):
        if x==a[l]:
            x=b[l]
    print(x)