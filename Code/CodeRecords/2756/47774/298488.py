import collections
n=int(input())
red_edges=eval(input())
blue_edges=eval(input())

r=collections.defaultdict(set)
b=collections.defaultdict(set)#红边蓝边
for i in red_edges:
    r[i[0]].add(i[1])
for i in blue_edges:
    b[i[0]].add(i[1])

step=0#步数
ans=[-1]*n#答案
ans[0]=0
v=set()#访问结点
v.add((0, 1))#在0点走红边
v.add((0, 0))#在0点走蓝边
q=[(0,1),(0,0)]#起始点
# BFS
while q:
    step+=1
    t=[]
    while q:
        node,color=q.pop()
        if color and node in r:
            for n in r[node]:
                if (n, 0) not in v:
                    v.add((n, 0))
                    if ans[n] == -1:
                        ans[n] = step
                    t.append((n, 0))
        elif not color and node in b:
            for n in b[node]:
                if (n,1) not in v:
                    if ans[n] == -1:
                        ans[n] = step
                    t.append((n, 1))
    q=t
print(ans)
