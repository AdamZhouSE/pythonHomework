def paint_numbers(arr,v):
    mincost=min(arr)
    if mincost>v:return -1
    max_dig=v//mincost
    if v % mincost==0:
        for i in range(8,-1,-1):
            if arr[i]==mincost:
                return str(i+1)*max_dig
    highest_bit=v-mincost*(max_dig-1)
    res=''
    for i in range(8,-1,-1):
        if arr[i]==highest_bit:
            res+=str(i+1)
            break
    for i in range(8,-1,-1):
        if arr[i]==mincost:
            res+=str(i+1)*(max_dig-1)
            return res


v=int(input())
arr=list(map(int,input().split()))
print(paint_numbers(arr,v))