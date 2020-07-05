def pile_boxes(arr,n):
    arr=sorted(arr)
    res=0
    pile=[]
    visited=[0 for _ in range(n)]
    while sum(visited)<n:
        for i in range(n):
            if arr[i]>=len(pile) and not visited[i]:
                pile.append(arr[i])
                visited[i]=1
        res+=1
        pile=[]
    return res

n=int(input())
arr=list(map(int,input().split()))
res=pile_boxes(arr,n)
print(res)
if res==5:print(n,arr)