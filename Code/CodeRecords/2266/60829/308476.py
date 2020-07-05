def dl(x):
    res=""
    for i in range(len(x)-1,0,-1):
        if  not x[i]==" ":
            break
    res=x[0:i+1]
    return res
n=int(input())
for i in range(2*n-1):
    n,k=[int(x) for x in dl(input()).split(" ")]
    x=n+k
a=[]
b=[]
for i in range(len(a)):
    if a[i]==x:
        x=b[i]
print(x)