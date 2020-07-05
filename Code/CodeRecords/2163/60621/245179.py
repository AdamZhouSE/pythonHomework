a=[]
a.append(int(input()))
a.append(int(input()))
b=[]
a[1]-=1
b=[i+1 for i in range(a[0])]
c=a[1]
length=a[0]-1
ans=""
while length>0:
    index=c//length
    c=c%length
    length-=1
    ans=ans+str(b[index])
    b.pop(index)
ans+=str(b[0])
print(ans)