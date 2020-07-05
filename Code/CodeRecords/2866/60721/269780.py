n=int(input())
lis=list(map(int,input().split(' ')))
num=[]
count=0
for i in range(lis.index(1),n):
    if(lis[i]==1):
        num.append(count)
        count=0
    else:
        count+=1
re=1
for x in num:
    re=re*(x+1)
print(re)