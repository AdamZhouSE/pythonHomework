def N(n,k):
    sum=0
    for i in range(1,n+1):
        sum=sum+k*i
    return sum
a=int(input())
aa=[]
for i in range(0,a):
    aa.append(int(input()))
res=[]
for i in range(0,a):
              res.append(N(N(aa[i],2),1)-N(N(aa[i]-1,2),1))
for i in range(0,a):
              print(res[i])