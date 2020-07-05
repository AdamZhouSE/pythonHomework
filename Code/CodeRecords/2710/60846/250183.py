def getAnswer(children,name,station,map):
    children.sort(key=lambda x:int(x))
    i=0
    while i<len(children) and name>children[i]:
        i+=1
    if i==len(children): return -1
    idx=i
    for i in range(idx,len(children)):
        if map[children[i]]<=station: return children[i]
    return -1

line=[int(x) for x in input().split()]
n=line[0]
q=line[1]
map={}
children=[]
for i in range(q):
    info=[x for x in input().split()]
    name=int(info[2])
    station=int(info[1])
    if info[0]=='M':
        children.append(name)
        map[name]=station
    elif info[0]=='D':
        print(getAnswer(children,name,station,map))

