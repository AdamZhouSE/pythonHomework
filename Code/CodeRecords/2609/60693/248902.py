def find_kth(arr:list,n,k):
    if k>n:return -1
    dict={}
    unique_nums=0
    for i in range(n):
        dict[arr[i]]=dict.get(arr[i],0)+1
    for i in range(n):
        if dict[arr[i]]==1:
            unique_nums+=1
        if unique_nums==k:
            return arr[i]
            break
    return -1

cases=int(input())
for i in range(cases):
    n_k=input().split()
    n,k=int(n_k[0]),int(n_k[1])
    arr=list(map(int,input().split()))
    print(find_kth(arr,n,k))