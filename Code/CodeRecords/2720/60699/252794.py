n=int(input())
connections=input()
connections=connections[1:(len(connections)-1)]
list1=[]
index=0
while index<len(connections):
    list1.append([int(connections[index+1]),int(connections[index+3])])
    index+=6
connections=list1
if len(connections) < n - 1:
    print(-1)
else:
    fa = [x for x in range(n)]


    def findset(x):
        if x != fa[x]:
            fa[x] = findset(fa[x])
        return fa[x]


    part = n
    for c0, c1 in connections:
        p, q = findset(c0), findset(c1)
        if p != q:
            part -= 1
            fa[p] = q

    print(part - 1)