n=int(input())
a=int(input())
b=int(input())
x=1
res=[]
for i in range(n):
    while((x%a!=0)&(x&b!=0)):
        x=x+1
    res.append(x)
    x=x+1
if(res[-1]==8):
    print(res)
    print(n)
    print(a)
    print(b)
print(res[-1])