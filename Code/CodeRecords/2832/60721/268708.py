n=int(input())
lis=list(map(int,input().split(' ')))
count=0
for i in range(1,n):
    if(lis[i]==i+1):
        count+=1
print(count+1)