def N(x):
    sum=0
    for i in range(1,x+1):
        sum=sum+(i*(i+1))//2
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