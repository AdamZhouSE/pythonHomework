def is_single_mount(arr:list,n):
    if n==1:return True
    judge=arr[0]-arr[1]
    if judge<0:
        # have part one
        index=-1
        for i in range(1,n-1):
            if arr[i]>=arr[i+1]:
                index=i
                break
        if index==-1:
            # only part one
            return True
        for i in range(index+1,n-1):
            if arr[i]<arr[i+1]:
                return False

    if judge==0:
        # without part one
        index=-1
        for i in range(1,n-1):
            if arr[i]<arr[i+1]:
                return False
            if arr[i]>arr[i+1]:
                index=i
                break
        if index==-1:
            # only part two
            return True
        for i in range(index+1,n-1):
            if arr[i]<=arr[i+1]:
                return False

    if judge>0:
        # only part three
        for i in range(1,n-1):
            if arr[i]<=arr[i+1]:
                return False
    return True

n=int(input())
arr=list(map(int,input().split()))
res=is_single_mount(arr,n)
if res:
    print('YES')
if not res:
    print('NO')
    