num=int(input())
sizes=list(map(int,input().split(' ')))
sum=0
for  i in sizes:
    sum=sum+i
k=sum%2
res=0
for i in sizes:
    if(i%2==k):
        res=res+1
print(res)