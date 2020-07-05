arr=list(map(int,input().strip().split(',')))
arr=sorted(arr)
maxn=max(arr[0]*arr[1]*arr[len(arr)-1],arr[len(arr)-3]*arr[len(arr)-2]*arr[len(arr)-1])
print(maxn)