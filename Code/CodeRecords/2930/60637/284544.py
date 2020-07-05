n=(int)(input())
arr=list(map(int,input().split(' ')))
sum=0
for i in range(1,len(arr)-1):
    if((arr[i]<arr[i-1] and arr[i]<arr[i+1])or(arr[i]>arr[i-1] and arr[i]>arr[i+1])):
        sum+=1
print(sum)