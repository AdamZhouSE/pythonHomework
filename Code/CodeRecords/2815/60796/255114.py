n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
re=0

for i in range(n):#先把所有大于1的数或小于-1的数变成1或-1
    if ls[i]>1:
        re=re+ls[i]-1
        ls[i]=1
    elif ls[i]<-1:
        re=re+(-1)-ls[i]
        ls[i]=-1

hasfu1=ls.__contains__(-1)
has1=ls.__contains__(1)
has0=ls.__contains__(0)

if has0:#有0在
    #三种情况：1.有1无-1 2.有-1无1 3.有1有-1
    #这些情况下0都要+1或-1
    re=re+ls.count(0)
else:#无0
    # 三种情况：1.有1无-1 2.有-1无1 3.有1有-1
    #1.有1无-1：
    if has1 and not hasfu1:#不需要动
        re=re+0
    #2.有-1无1
    if hasfu1 and not has1:
        if ls.count(-1)%2==1:#需要有一个-1变成1
            re=re+2
    #3.有-1有1
    if hasfu1 and has1:
        if ls.count(-1)%2==1:#需要有一个-1变成1
            re=re+2

print(re)








