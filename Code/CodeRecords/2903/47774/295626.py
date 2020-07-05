arr=eval(input())
res=[0]
state=set()
arr=[set(i) for i in arr if len(i)==len(set(i))]

def dfs(state,t):
    if len(state)>res[0]:
        res[0]=len(state)
    for i in range(t,len(arr)):
        if len(state)+len(arr[i])==len(state|arr[i]):
            dfs(state|arr[i],i+1)
dfs(state,0)          
print(res[0])