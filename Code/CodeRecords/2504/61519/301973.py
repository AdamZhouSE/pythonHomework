num=list(input().split(","))
num[0]=num[0][2:len(num[0])]
num[-1]=num[-1][0:-2]
n=[]
k=1
for i in range(1,len(num)-1):
    if k==1:
        num[i]=num[i][0:-1]
        k=2
        continue
    if k==2:
        num[i]=num[i][1:len(num[i])]
        k=1
        continue
tem=[0,0]
for i in range(int(len(num)/2)):
    tem[0]=int(num[2*i])
    tem[1]=int(num[2*i+1])
    n.append(tem)
    tem=[0,0]
for i in range(len(n)):
    n[i][0]=int(n[i][0])
    n[i][1]=int(n[i][1])
tem=n[0][0]**2+n[0][1]**2
for i in range(len(n)):
    if n[i][0]**2+n[i][1]**2<tem:
        tem=n[i][0]**2+n[i][1]**2
k=int(input())
res=[]
while k>0:
    for i in range(len(n)):
        if n[i][0]**2+n[i][1]**2==tem:
            res.append(n[i])
            k-=1

print(res)