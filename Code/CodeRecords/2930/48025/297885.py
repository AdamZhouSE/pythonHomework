n=int(input())
arr=list(map(int,input().split()))
counter=0
for i in range(1,len(arr)-1):
    if((arr[i]>arr[i-1])and(arr[i]>arr[i+1])):
        counter+=1
    elif((arr[i]<arr[i-1])and(arr[i]<arr[i+1])):
        counter+=1
print(counter)