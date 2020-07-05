import numpy as np
[k,n]=list(map(int,input().split(",")))
ans=[]
def dfs(ans,temp,start):
    if len(temp)==k:
        if np.sum(temp)==n and temp not in ans:
            ans.append(temp.copy())
        return
    for i in range(start,10):
        temp.append(i)
        dfs(ans,temp,i+1)
        temp.pop()
dfs(ans,[],1)
print(ans)


