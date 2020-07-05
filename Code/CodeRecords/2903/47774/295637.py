arr=eval(input())
res=0
state=set()
arr=[set(i) for i in arr if len(i)==len(set(i))]

def dfs(state,t):
    global res
    res=max(len(state),res)
    for i in range(t,len(arr)):
        if len(state)+len(arr[i])==len(state|arr[i]):
            dfs(state|arr[i],i+1)
dfs(state,0)          
print(res)