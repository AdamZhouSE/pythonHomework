# 28
n=int(input())
arr=input().split()
arr=list(map(int,arr))
count=0
for i in range(0,len(arr)):
    if arr[i]>n:
        count = count + arr[i] - n
        arr[i]=n
    elif arr[i]<1:
        count = count + 1 - arr[i]
        arr[i]=1
for j in range(1,n+1):
    diff=[arr[k]-j for k in range(0,len(arr))]
    count = count + abs(min(diff))
    arr.remove(j+min(diff))
    diff.remove(min(diff))
print(count)