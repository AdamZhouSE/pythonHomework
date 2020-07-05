n=int(input())
lis=[]
ans=0
for i in range(0,n):
    lis.append(list(map(int,input().split(" "))))
temp=[]
for i in lis:
    temp.append(i[0])
    temp.append(i[1])
temp=sorted(temp)
street=[]
for i in range(0,max(temp)):
    street.append(0)
for i in lis:
    for j in range(i[0]-1,i[1]-1):
        street[j]=i[2] if i[2]>street[j] else street[j]
ans=0
for i in street:
    ans+=i
print(ans)