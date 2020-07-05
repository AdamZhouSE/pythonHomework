arr=eval(input())
res=0
state=set()
arr=[set(i) for i in arr if len(i)==len(set(i))]

def dfs(state,t):
    global res#指明此处 res 是全局变量
    res=max(len(state),res)
    for i in range(t,len(arr)):
        #没有重复字母 
        flag=1
        for j in state:
            if j in arr[i]:
                flag=0
                break
        if flag==1:
            dfs(state|arr[i],i+1)  #|两个 set 合并     
dfs(state,0)          
print(res)