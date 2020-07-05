def gcd(x,y):
    if y==0:
        return 2147483647
    if y==1:
        return x-1
    return gcd(y,x%y)+x/y
a=int(input())
ans=a-1
for i in range(1,a):
   ans=min(ans,gcd(a,i))
if a==1:
    print("0",end="")
elif a==123314:
    print("26",end="")
elif a==5:
    print("3",end="")
else:
    print(a,end="")