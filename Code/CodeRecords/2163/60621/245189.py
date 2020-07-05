a=[]
a.append(int(input()))
a.append(int(input()))
b=[]
a[1]-=1
b=[i+1 for i in range(a[0])]
c=a[1]
length=1
ans=""
for i in range(1,a[0]+1):
    length*=i
num=a[0]
while length>1:
    length=int(length/num)
    index=c//length
    c=c%length
    ans=ans+str(b[index])
    b.pop(index)
    num-=1
ans+=str(b[0])
print(ans)