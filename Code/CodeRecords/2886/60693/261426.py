def match_socks(arr):
    maxnum=0
    dsocks=[]
    for i in range(len(arr)):
        if arr[i] in dsocks:
            dsocks.remove(arr[i])
            break
        else:
            dsocks.append(arr[i])
            if maxnum<len(dsocks):
                maxnum=len(dsocks)
    return maxnum

p=int(input())
arr=list(map(int,input().split()))
print(match_socks(arr))