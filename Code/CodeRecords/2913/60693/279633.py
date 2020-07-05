def getAllZero(arr,n):
    if sum(arr)%2==0:
        return True
    return False

n=int(input())
arr=list(map(int,input().split()))
res=getAllZero(arr,n)
if res:print('YES')
else:print('NO')
    