n=int(input())
a=sorted(list(map(int,input().split())))
num=0
qu=[]
if a[0]==1:
    qu.append(1)
else:
    for i in range(1,int(a[0]**0.5)):
        if a[0]%i==0:
            qu.append(i)
            qu.append(a[0]//i)
for i in qu:
    ok=True
    for j in a:
        if j%i!=0:
            ok=False
            break
    if ok==True:
        num+=1
print(num)