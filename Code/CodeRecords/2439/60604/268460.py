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
    fa=None
    waytoch=0
    def __init__(self,name,ch,waytoch):
        self.name=name
        if ch!=None:
            self.ch=way(ch,None,0)      
            self.ch.fa=self
        self.waytoch=waytoch

n=int(input())
node=[]
for I in range(n-1):
    x=input().split()
    print(x)
    for i in range(len(x)):
        x[i]=int(x[i])
    find=False
    for i in node:
        if i.name==x[0]:
            find=True
            tmp=way(x[0],x[1],x[2])
            
            u=False
            for j in node:
                if j.name==tmp.ch.name:
                    i.ch=j
                    i.waytoch=tmp.waytoch
                    u=True
            if not u:
                
                node.append(tmp)

        elif i.name==x[1]:
            print(x)
            find=True
            tmp=way(x[0],x[1],x[2])
            
            u=False
            for j in node:
                if j.name==tmp.name:
                    j.ch=i
                    j.waytoch=tmp.waytoch
                    u=True
            if not u:
                tmp.ch=i
                node.append(tmp)
                
        
    if not find:
        tmp=way(x[0],x[1],x[2])
        node.append(tmp)
        node.append(tmp.ch)
                  
for tmp in node:
    print(tmp.name,tmp.ch==None,tmp.waytoch)
for i in node:
    print(i.name)
q=int(input())     
#print(q)
for I in range(q):
    x=input().split()
    begin=2
    end=3
    #print(findway(road,begin,end))
























































