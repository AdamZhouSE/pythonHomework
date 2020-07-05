# 并查集
disjointSet = [0]*(27)# 26个小写字母
for i in range(1,27):
    disjointSet[i] = i
def find(x):
    global disjointSet
    if(disjointSet[x] == x):
        return x
    else:
        disjointSet[x] = find(disjointSet[x])
        return disjointSet[x]

equations = eval(input())
res = True
for i in equations:# 先合并
    x = i[0]
    y = i[-1]
    if i[1] == '=':
        disjointSet[find(ord(x)-ord('a'))] = find(ord(y)-ord('a'))# combine
for i in equations:# 先合并
    x = i[0]
    y = i[-1]
    if i[1] == '!':
        if find(ord(x)-ord('a')) == find(ord(y)-ord('a')):
            res = False
            break
if res:
    print("true")
else:
    print("false")





