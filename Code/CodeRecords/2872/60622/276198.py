n=int(input())
arr=input().split()

for i in range(0,len(arr)-1):
    if arr[i]==arr[i+1]:
        arr.pop(i)
        i=i-1
print(n-len(arr))