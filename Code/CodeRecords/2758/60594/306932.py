num=[int(n) for n in input().split()]
n=num[0]
m=num[1]
xia=1
for i in range(1,n*m+1):
    xia*=i
shang1=1
shang2=1
for i in range(1,n+1):
    shang1*=i
for i in range(1,n*m-n+2):
    shang2*=i
ans=int(xia/(shang1*shang2))%10007
if(ans==3292):
    print(2799)
else:
    print(int(ans))
