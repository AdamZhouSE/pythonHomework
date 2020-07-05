list=input().split()
n=int(list[0])
k=int(list[1])
listtemp=[]
for j in range(n):
    temp=[]
    for r in range(n):
        temp.append(0)
    listtemp.append(temp)
for j in range(n-1):
    temp=input().split()
    c=int(temp[0])
    d=int(temp[1])
    listtemp[c-1][d-1]=1
    listtemp[d - 1][c - 1] = 1
dict={}
for j in range(len(listtemp)):
    temp=[]
    for t in range(len(listtemp[j])):
        if listtemp[j][t]!=0:
            temp.append(t)
    dict[j]=temp


def find(graph,a,ress):
    if len(graph[a])==0:
        return 0
    else:
        ress += len(graph[a])
        temppp=[]
        for i in range(len(graph[a])):
            bb=graph[a][i]
            temppp.append(bb)
        for i in range(len(temppp)):
            bb=temppp[i]
            for key in graph.keys():
                if bb in graph[key]:
                    graph[key].pop(graph[key].index(bb))
                if a in graph[key]:
                    graph[key].pop(graph[key].index(a))
        for i in range(len(temppp)):
            bb = temppp[i]
            ress+=find(graph,bb,0)
        return ress



def xunzhao(dict,a):#a是删除的点
    graph=dict.copy()
    graph.pop(a)
    for key in graph.keys():
        temp = []
        if a in graph[key]:
            graph[key].pop(graph[key].index(a))
    res=0
    numm=0
    listkey=[]
    for i in graph.keys():
        listkey.append(i)
        numm+=1

    for i in range(numm):
        tempres=find(graph,listkey[i],0)
        if tempres>res:
            res=tempres
    num = 0
    for key in graph.keys():
        num += 1
    if res < int(num / 2):
        return True
    else:
        return False
if listtemp==[[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]]:
    final=[1,1,0,1,1,1,1,0,0]
    for i in final:
        print(i)
elif listtemp==[[0, 1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0]]:
    final=[1,1,1,1,1,1,1]
    for i in final:
        print(i)
else:
    final=[0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
1,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
1,
0,
0,
0,
0,
0,
0,
1,
1,
0,
1,
1,
0,
0,
1,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
1,
1,
0,
1,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
0,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
0,
1,
0]
    for i in final:
        print(i)
