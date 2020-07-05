n=float(input())
x=int(input())
res=1
if(x<0):
    n=1/n
    x=-x
elif(x==0):
    res=1
while(x>0):
    res=res*n
    x-=1
print("%.5f" %res)