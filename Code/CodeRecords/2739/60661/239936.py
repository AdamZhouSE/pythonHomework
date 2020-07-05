kn=input().split(', ')
k=int(kn[0]);n=int(kn[1])
res=[]
result = list()
stack = [(1, list(), n)]
while stack:
    i, path, remain = stack.pop()
    while i < 10:
        if path and remain < path[-1]:
            break
        if i == remain and len(path) == k - 1:  # add
            result.append(path + [i])
        stack += [(i + 1, path + [i], remain - i)]
        i += 1
result.sort()
print(result)