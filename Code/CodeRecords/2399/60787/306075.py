def cal(n):
    re=1
    for i in range(2,n+1):
        re*=i
    return re

t=int(input())
for ex in range(0,t):
    n,m,l,r=map(int,input().split(" "))
    num=[i for i in input().split(" ")]
    count=[]
    for i in range(l,r+1):
        count.append(0)
        for j in num:
            if j==str(i):
                count[-1]+=1
    #添加序列
    temp=0
    current=0
    while True:
        while current in count:
            num.append(str(count.index(current)+l))
            count[count.index(current)]+=1
            temp+=1
            if temp==m:
                break
        else:
            current+=1
            continue
        break
    re=cal(len(num))
    #计算重复
    count=[]
    num_count=[]
    for i in num:
        if i in count:
            num_count[count.index(i)]+=1
        else:
            count.append(i)
            num_count.append(1)
    for i in num_count:
        re=re//cal(i)
    print(re%998244353)