arr=list(map(int,input().split(",")))
arr.sort()
k=int(input())
print(arr[len(arr)-k])