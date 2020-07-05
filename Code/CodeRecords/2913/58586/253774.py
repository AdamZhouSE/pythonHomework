import numpy as np
nums=int(input())
arr=list(map(int,input().split(" ")))
sum=np.sum(arr)
if sum%2:
    print("NO")
else:
    print("YES")