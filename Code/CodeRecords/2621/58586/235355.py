arr=list(map(int,input().split(",")))
i=0
sum=0
max=-1000000007
for i in range(len(arr)):
    sum+=arr[i]
    if sum<0:
        sum=0
    if(sum>max):
         max=sum
    i+=1
print(max)