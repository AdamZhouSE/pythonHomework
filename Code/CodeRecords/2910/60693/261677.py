def revovle_right(arr,n):
    curhei=max(arr[0])
    for i in range(1,n):
        if min(arr[i])>curhei:
            return False
        if max(arr[i])<=curhei:
            curhei=max(arr[i])
        else:
            curhei=min(arr[i])
    return True

n=int(input())
arr=[]
for i in range(n):
    rec=list(map(int,input().split()))
    arr.append(rec)

if revovle_right(arr,n):print('YES')
else:print('NO')