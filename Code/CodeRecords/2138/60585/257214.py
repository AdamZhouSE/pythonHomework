arr=list(map(int,input().strip().split(',')))
k=eval(input())
n=len(arr)
isM=False
for i in range(0,n-1):
    j=i+1
    temp=arr[i]
    while j<n:
        temp+=arr[j]
        j+=1
        if temp%k==0:
            isM=True
            break
    if isM:
        break
print(isM)