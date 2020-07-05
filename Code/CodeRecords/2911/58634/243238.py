n,m = map(int, input().split())
disjointSet = [0]*(n+1)
gold = [0]*(n+1)
def find(x):
    global disjointSet
    if(disjointSet[x] == x):
        return x
    else:
        disjointSet[x] = find(disjointSet[x])
        return disjointSet[x]
temp = [int(i) for i in input().split(" ")]
for i in range(1,n+1):
    disjointSet[i] = i
    gold[i] = temp[i-1]
#初始化完成
for i in range(m):
    a, b = map(int, input().split())
    fa = find(a)
    fb = find(b)
    disjointSet[fa] = fb
    if (gold[fb]>gold[fa]):
        gold[fb] = gold[fa]#最小黄金
result = 0
for i in range(1,n+1):
    if(disjointSet[i] == i):
        result +=gold[i]
print(result)