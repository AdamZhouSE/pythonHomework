def N(n):
    sum=2
    if n==1:
        return sum
    for i in range(2,n+1):
        sum=sum+x(i-1)
    return sum
def x(n):
    sum=2
    count=0
    for i in range(1,n+1):
        count=count+6
        sum=sum+count
    return sum
a=int(input())
aa=[]
for i in range(0,a):
    aa.append(int(input()))
res=[]
for i in range(0,a):
              res.append(N(aa[i]))
for i in range(0,a):
              print(res[i])