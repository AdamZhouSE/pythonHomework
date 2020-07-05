def shortest_subarr():
    arr=list(map(int,input().replace(']','').replace('[','').split(',')))
    K=int(input())
    if sum(arr)<K:
        return -1
    length=0
    l,r=0,1
    ans=len(arr)
    while r<=len(arr):
        if sum(arr[l:r])<K:
            r+=1
        else:
            ans=min(ans,r-l)
            l+=1
    return ans


print(shortest_subarr())