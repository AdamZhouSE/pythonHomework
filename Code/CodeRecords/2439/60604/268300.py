'''def findway(road,begin,end):
    res=[]
    print(111)
    if begin==end:
        return 0
    else:
        for i in range(len(road)):
            if road[i][0]==begin :
                if road[i][1]==end:
                    return road[i][2]
                else:
                    begin=road[i][1]
                    j=0
                    tmp=[]
                    while j<len(road) and j!=i:
                        tmp.append(road[j])
                    return road[i][2]^findway(tmp,begin,end)
            elif road[i][1]==begin:
                if road[i][0]==end:
                    return road[i][2]
                else:
                    begin=road[i][0]
                    j=0
                    tmp=[]
                    while j<len(road) and j!=i:
                        tmp.append(road[j])
                        print(tmp)
                    return road[i][2]^findway(tmp,begin,end)
            elif road[i][1]==end:
                if road[i][0]==begin:
                    return road[i][2]
                else:
                    end=road[i][0]
                    j=0
                    tmp=[]
                    while j<len(road) and j!=i:
                        tmp.append(road[j])
                    return road[i][2]^findway(tmp,begin,end)
            elif road[i][0]==end:
                if road[i][1]==begin:
                    return road[i][2]
                else:
                    end=road[i][1]
                    j=0
                    tmp=[]
                    while j<len(road) and j!=i:
                        tmp.append(road[j])
                    return road[i][2]^findway(tmp,begin,end)
                    '''
class way:
    name=0
    ch=None
    waytoch=0
    def __init__(self,name,ch,waytoch):
        self.name=name
        self.ch=ch
        self.waytoch=0
n=int(input())
road=[]
for I in range(n-1):
    x=input().split()
    for i in range(len(x)):
        x[i]=int(x[i])
    road.append(x)
    print(road)
q=int(input())     
print(q)
for I in range(q):
    print(1)
    x=input()
    print(x)
    begin=2
    end=3
    print(findway(road,begin,end))
























































