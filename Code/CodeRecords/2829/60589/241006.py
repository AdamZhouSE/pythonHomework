n=int(input())
arr=list(map(int,input().split(' ')))
arr.sort()
a=arr[len(arr)-2]-arr[0]
b=arr[len(arr)-1]-arr[1]
print(a if a<b else b)