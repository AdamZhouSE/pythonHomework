def flow(i,j):
    if alabel[i][0]==1:
        return flows[alabel[i][1]][alabel[j][1]][0]
    elif alabel[i][0]==3:
        return flows[alabel[j][1]][alabel[i][1]][1]
    else:
        if alabel[j][0] == 1:
            return flows[alabel[j][1]][0][1]
        else:
            return flows[0][alabel[j][1]][0]

n,m=map(int,input().split())
Sum=0
g=[]
label=[0]
alabel=[[0,0],[0,0]]
for j in range(n):
    g.append(list(map(lambda x:int(x) if x!='*' else x,list(input().split()[0]))))
for i in range(n):
    for j in range(m):
        if g[i][j]==2:
            g[i][j]='*'
            Sum+=1
        elif g[i][j]==1:
            alabel[0][0]+=1
            alabel.insert(-1,[1,alabel[0][0]])
            label.append(i * m + j + 1)
        elif g[i][j]==3:
            alabel[-1][0]+=1
            alabel.insert(-1,[3,alabel[-1][0]])
            label.append(i * m + j + 1)
if alabel[0][0]==0 or alabel[-1][0]==0:
    print(Sum)
else:
    label.append(n * m + 1)
    le = len(label)
    flows = [[[[0, 0], [0, 0]] for j in range(alabel[-1][0] + 1)] for i in range(alabel[0][0] + 1)]
    alabel[0][0] = str(alabel[0][0])
    alabel[-1][0] = str(alabel[-1][0])
    net = [[] for i in range(le)]
    for i in range(n):
        for j in range(m):
            if g[i][j] != '*':
                index = label.index(i * m + j + 1)
                if i > 0 and g[i - 1][j] == 4 - g[i][j]:
                    tmp = label.index((i - 1) * m + j + 1)
                    net[index].append(tmp)
                if i < n - 1 and g[i + 1][j] == 4 - g[i][j]:
                    tmp = label.index((i + 1) * m + j + 1)
                    net[index].append(tmp)
                if j > 0 and g[i][j - 1] == 4 - g[i][j]:
                    tmp = label.index(i * m + j)
                    net[index].append(tmp)
                if j < m - 1 and g[i][j + 1] == 4 - g[i][j]:
                    tmp = label.index(i * m + j + 2)
                    net[index].append(tmp)
    for i in range(le):
        if alabel[i][0] == 1:
            for j in net[i]:
                flows[alabel[i][1]][alabel[j][1]] = [[1, 0], [1, 0]]
    for i in range(1, le - 1):
        if alabel[i][0] == 1:
            net[0].append(i)
            flows[alabel[i][1]][0] = [[1, 0], [1, 0]]
        else:
            net[i].append(le - 1)
            flows[0][alabel[i][1]] = [[1, 0], [1, 0]]
    finished = False
    while True:
        labeled = [[] for i in range(le)]
        labeled[0] = [max([flows[i][0][0][0] for i in range(len(flows))]), -1]
        buffer = [0]
        while True:
            buffertmp = []
            for j in buffer:
                for i in net[j]:
                    tmp = flow(j, i)
                    tmp = tmp[0] - tmp[1] if tmp[1] >= 0 else -tmp[1]
                    if not labeled[i] and tmp > 0:
                        buffertmp.append(i)
                        labeled[i] += [min(tmp, labeled[j][0]), j]
                        if i == le - 1:
                            finished = True
                            break
                if finished:
                    finished = False
                    break
            if labeled[-1]:
                e = labeled[-1][0]
                Sum += e
                now = le - 1
                while now:
                    last = labeled[now][1]
                    flow(last, now)[1] += e
                    flow(now, last)[1] -= e
                    now = last
                break
            if not buffertmp:
                finished = True
                break
            buffer = buffertmp
        if finished:
            break
    print(Sum)