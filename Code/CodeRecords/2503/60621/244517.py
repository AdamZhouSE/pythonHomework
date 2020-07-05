a=eval(input())
b=[]
for i in range(a):
    b.append([])
for i in range(a-1):
    c=[int(x)-1 for x in input().split()]
    b[c[0]].append(c[1])
    b[c[1]].append(c[0])
maxLen=0
last=0
def dp(x,path:list):
    global maxLen ,last
    path.append(x)
    if (len(path) > maxLen):
        maxLen = len(path)
        last = path[len(path) - 1]
    if len(b[x])==0:
        path.remove(x)
        return 0
    for i in b[x]:
        if i not in path:
            dp(i,path)

    path.remove(x)

dp(0,[])
maxLen=0
tem=last;last=0
dp(tem,[])

print(maxLen-1)