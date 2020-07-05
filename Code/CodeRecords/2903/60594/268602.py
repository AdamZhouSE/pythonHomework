arr=eval(input())
visited=set()
all=[]
def dfs(start, tmp):
    all.append(tmp)
    if start >= len(arr):
        return
    for i in range(start + 1, len(arr)):
        if not (set(tmp) & set(arr[i])):
            visited.add(arr[i])
            dfs(i, tmp + arr[i])
            visited.remove(arr[i])
for i, s in enumerate(arr):
    visited.add(s)
    dfs(i, s)
    visited.remove(s)
max=0
for i in all:
    if len(i)>max:
        max=len(i)
print(max)


