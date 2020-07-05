#递归
def dfs(i, tmp):
    if i >= len(arr):
        res=len(tmp)
    else:
        if not (set(tmp) & set(arr[i])):
            res=max(dfs(i+1,tmp+arr[i]),dfs(i+1,tmp))
        else:
            res=dfs(i+1, tmp)

arr=eval(input())
res=0
t = []
for s in arr:
    if len(set(s)) == len(s):
        t.append(s)
arr = t[:]
res=dfs(0,'')
print(res)