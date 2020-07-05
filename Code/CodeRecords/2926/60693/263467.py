def pockets(arr,n):
    dict={}
    for i in range(n):
        dict[arr[i]]=dict.get(arr[i],0)+1
    return max(dict.values())

n=int(input())
arr=list(map(int,input().split()))
print(pockets(arr,n))