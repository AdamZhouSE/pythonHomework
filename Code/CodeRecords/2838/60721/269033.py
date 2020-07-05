n=int(input())
lis=list(map(int,input().split(' ')))
lis.sort()
num=[]
for i in range(0,int(n/2)):
    num.append(lis[i]+lis[n-i-1])
re=0
for x in num:
    re=re+x*x
print(re)