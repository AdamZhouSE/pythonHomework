n=int(input())
arr=list(map(int,input().split()))
res=[]
for i in range(n-1,-1,-1):
    if arr[i] not in res:
        res.append(arr[i])
res.reverse()
print(len(res))
print(' '.join(str(i) for i in res))