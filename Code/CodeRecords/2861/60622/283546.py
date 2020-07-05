n=int(input())
arr=list(map(int,input().split()))
arr.sort()
count=0
i=0
while i<n-1:
    count+=abs(arr[i]-arr[i+1])
    i=i+2
print(count)