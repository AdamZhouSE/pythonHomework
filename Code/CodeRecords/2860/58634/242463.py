#并查集
n = int(input())
disjointSet = [0]*(n+1)
x = [0]*(n+1)
y = [0]*(n+1)
result = 0
def find(x):
    global disjointSet
    if(disjointSet[x] == x):
        return x
    else:
        disjointSet[x] = find(disjointSet[x])
        return disjointSet[x]
for i in range(1,n+1):
    x[i],y[i] = map(int, input().split())
for i in range(1,n+1):
    disjointSet[i] = i
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if(x[i] == x[j] or y[i] == y[j]):
            disjointSet[find(i)] = find(j) #合并
for i in range(1,n+1):
    if(disjointSet[i] == i):
        result+=1
print(result-1)