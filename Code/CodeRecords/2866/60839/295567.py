n=int(input())
lis=list(map(int,input().split(" ")))

temp2=False
for i in lis:
    if i==1:
        temp2=True
for i in range(0,len(lis)):
    if lis[i]==1:
        del lis[0:i]
        break
for i in range(len(lis)-1,-1,-1):
    if lis[i]==1:
        del lis[i+1:]
        break
judge=False
count=[]
temp=0
for i in range(1,len(lis)):
    if lis[i]==1:
        judge==True
        count.append(temp)
        temp=0
    else:
        temp+=1
ans=1
if not temp2:
    print(0)
else:
    for i in count:
        ans=ans*(i+1)
    print(ans)