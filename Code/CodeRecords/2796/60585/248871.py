import math
n=eval(input())
arr=list(map(int,input().strip().split(' ')))
arr=sorted(arr)
for i in range(len(arr)-1,-1,-1):
    if arr[i]<0:
        break
    m=int(math.sqrt(arr[i]))
    if arr[i]!=m*m:
        break
print(arr[i])