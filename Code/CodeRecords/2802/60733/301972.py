n,m = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(n):
    arr[i] = (arr[i]-1)//m
arr.reverse()
print(n - arr.index(max(arr)))