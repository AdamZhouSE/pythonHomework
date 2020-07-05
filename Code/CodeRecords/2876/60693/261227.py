def turning_off(arr,n):
    if n<3:return 0
    res=0
    for i in range(1,n-1):
        if arr[i]==0 and arr[i-1]==1 and arr[i+1]==1:
            res+=1
            arr[i+1]=0
    return res

n=int(input())
arr=list(map(int,input().split()))
print(turning_off(arr,n))