def exist(arr):
    for x in range(len(arr)):
        sum=0
        if x==len(arr)-2:
            if x==0 or x+arr[-1]==0:
                return True
            else:break
        else:
            for y in range(x,len(arr)):
                sum+=arr[y]
                if sum==0:return True
    return False
                
cases=int(input())
for i in range(cases):
    n=int(input())
    arr=list(map(int,input().split()))
    if exist(arr):print('Yes')
    else:print('No')
        