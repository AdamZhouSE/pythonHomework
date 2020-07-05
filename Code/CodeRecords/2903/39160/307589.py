arr = eval(input())

t = []
for s in arr:
    if len(set(s)) == len(s):
        t.append(s)
    arr = t[:]

def dfs(i, tmp):
    if i >= len(arr):
        return len(tmp)
    else:
        if not (set(tmp) & set(arr[i])):
            return max(dfs(i+1,tmp+arr[i]),dfs(i+1,tmp))
        else:
            return dfs(i + 1, tmp)

l=dfs(0,'')
print(l)

