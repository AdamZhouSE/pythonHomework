n=int(input())-1
k=int(input())
dd=[]
for i in range(1, n + 2):
    dd.append(i)
res=""
while n>=0:
    ll = 1
    for i in range(1, n + 1):
        ll = ll * i
    if  not ll==1:
        xx = k // ll
    else:
        xx=0
    n=n-1
    res=res+str(dd[xx])
    for j in range(xx,len(dd)-1):
        temp=dd[j]
        dd[j]=dd[j+1]
        dd[j+1]=temp
    k=k-xx*ll
print(res)