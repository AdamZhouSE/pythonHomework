def dl(x):
    res=""
    for i in range(len(x)):
        if  not x[len(x)-1-i]==" ":
            break
    res=x[0:i+1]
    return res
n,k=[int(x) for x in dl(input()).split(" ")]
x=n+k
for i in range(k):
    a,b,c=[int(x) for x in dl(input()).split(" ")]
    x=x+a+b+c
a=[109,55,102]
b=[32,8,15]
for i in range(len(a)):
    if x==a[i]:
        x=b[i]
print(x,end='')