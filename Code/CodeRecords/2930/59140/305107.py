n=int(input())
arr = [int(x) for x in input().split(" ")]
result=0
for i in range(1,n-1):
    if arr[i-1]>arr[i]<arr[i+1]:result+=1
    if arr[i-1]<arr[i]>arr[i+1]:result+=1
print(result)