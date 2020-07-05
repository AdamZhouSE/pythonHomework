def remove_it(arr,n):
    if n < 6: return n
    standard=[4,8,15,16,23,42]
    res=n
    visited=[0 for _ in range(n)]
    while True:
        tmp=[]
        for i in range(len(arr)):
            if arr[i]==standard[len(tmp)] and arr[i] not in tmp and not visited[i]:
                tmp.append(arr[i])
                visited[i]=1
                if len(tmp)==6:
                    res-=6
                    break
        if len(tmp)!=6:return res

n=int(input())
arr=list(map(int,input().split()))
print(remove_it(arr,n))