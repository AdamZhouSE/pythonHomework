def N(n):
    sum=0
    count=3
    for i in range(1,n+1):
        sum=sum+count
        count=count+4
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