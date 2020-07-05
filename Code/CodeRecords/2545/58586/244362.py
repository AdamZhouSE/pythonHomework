import numpy as np
nums=int(input())
def dfs(arr,temp,start):
    if len(temp)>0 and np.sum(temp)==0:
        return True
    for i in range(start,len(arr)):
        temp.append(arr[i])
        if dfs(arr,temp,i+1):
            return True
        temp.pop()
    return False
for i in range(nums):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    temp=[]
    if dfs(arr,temp,0):
        print("Yes")
    else:
        print("No")





