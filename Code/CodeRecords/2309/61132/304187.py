n,m=map(int,input().split())
Sum=0
g=[]
label=[0]
for j in range(m):
    g.append(list(map(lambda x:int(x) if x!='*' else x,list(input().split()[0]))))
for i in range(n):
    for j in range(m):
        if g[i][j]==2:
            g[i][j]='*'
            Sum+=1
        elif g[i][j]!='*':
            label.append(i*m+j+1)
N=n*m+1
label.append(N)
le=len(label)
flow=[[[0,0] for j in range(le)]for i in range(le)]
net=[[] for i in range(le)]
for i in range(n):
    for j in range(m):
        if g[i][j]!='*':
            index=label.index(i * m + j + 1)
            if i>0 and g[i-1][j]==4-g[i][j]:
                tmp = label.index((i - 1) * m + j + 1)
                net[index].append(tmp)
            if i<n-1 and g[i+1][j]==4-g[i][j]:
                tmp = label.index((i + 1) * m + j + 1)
                net[index].append(tmp)
            if j>0 and g[i][j-1]==4-g[i][j]:
                tmp = label.index(i * m + j )
                net[index].append(tmp)
            if j<m-1 and g[i][j+1]==4-g[i][j]:
                tmp = label.index(i * m + j + 2)
                net[index].append(tmp)
for i in range(le):
    for j in net[i]:
        flow[i][j]=flow[j][i]=[1,0]
for i in range(1,le-1):
    tmp=label[i]-1
    tmp=g[tmp//m][tmp%m]
    if tmp==1:
        net[0].append(i)
        flow[0][i]=[1,0]
        flow[i][0]=[1,0]
    else:
        net[i].append(le-1)
        flow[-1][i]=[1,0]
        flow[i][-1]=[1,0]
finished=False
while True:
    labeled=[[] for i in range(le)]
    labeled[0]=[sum([flow[0][i][0] for i in range(le)]),-1]
    buffer=[0]
    while True:
        buffertmp=[]
        for j in buffer:
            if finished:
                finished=False
                break
            for i in net[j]:
                tmp = flow[j][i]
                tmp = tmp[0] - tmp[1] if tmp[1] >= 0 else -tmp[1]
                if not labeled[i] and tmp > 0:
                    buffertmp.append(i)
                    labeled[i]+=[min(tmp,labeled[j][0]),j]
                    if i==le-1:
                        finished=True
                        break
        if labeled[-1]:
            e=labeled[-1][0]
            Sum+=e
            now=-1
            while now:
                last = labeled[now][1]
                flow[last][now][1]+=e
                flow[now][last][1]-=e
                now=last
            break
        if not buffertmp:
            finished=True
            break
        buffer=buffertmp
    if finished:
        break
print(Sum)