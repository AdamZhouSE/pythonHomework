n=int(input())
arr=input().strip().split(' ')
arr=[int(i) for i in arr]

count=0
for i in range(1,n-1):
    if arr[i-1]<arr[i]>arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
        count+=1
print(count)