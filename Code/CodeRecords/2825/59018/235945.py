n=int(input())
a=[]
for i in range(n):
    x=input().split(' ')           #第i行的str型
    b=[int(y) for y in x]          #第i行的int型
    count=0
    for j in range(len(b)):
        count=count+b[j]           
    a.append(count)                #a[i]=count i
c=sorted(a,reverse=True)
print(c.index(a[0])+1)