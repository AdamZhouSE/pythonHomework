arr=list(map(int,input().split(",")))
K=int(input())
print(max(max(arr)-min(arr)-2*K,0))