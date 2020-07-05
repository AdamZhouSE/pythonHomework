a=int(input())
b=[]
b=input().split()
l=[]
sum1=0
for i in range(len(b)):
    l.append(int(b[i]))
    sum1=sum1+l[i]
res=sum1/a
res=format(res,'.6f')
print(res)