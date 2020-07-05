n=int(input())
lis=list(map(int,input().split(' ')))
count=0
max=0
for i in range(0,n):
    if(lis[i]>max):
        max=lis[i]
    if(lis[i]==i+1):
        if(i+1==max):
            count+=1
print(count)