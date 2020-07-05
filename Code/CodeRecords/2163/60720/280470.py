import math
n=int(input())
k=int(input())
list0=[i for i in range(n+1)]
s=''
def jie(num):
    sum=1
    while(num>1):
        sum*=num
        num-=1
    return sum
for i in range(n):
    sh=math.ceil(k/jie(n-i-1))
    s=s+str(list0[sh])
    del list0[sh]
    k=k-(sh-1)*jie(n-1-i)
print(s)

