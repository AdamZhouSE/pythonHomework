n=int(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
    arr[i]=arr[i]%2
print(min(arr.count(0),arr.count(1)))
