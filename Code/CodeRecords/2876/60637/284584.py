n=(int)(input())
arr=list(map(int,input().split(' ')))
sum=0
for i in range(1,n-1):
    if(arr[i]==0 and arr[i-1]==1 and arr[i+1]==1):
        arr[i+1]=0
        sum+=1
print(sum)
