from itertools import combinations
def create_tree(sources):
    lists=[]
    source=[]
    for i in sources:
        source.append([i[0],i[1]])
    for i in range(pow(2,10)):
        lists.append("*")
    if(source[0][0]!="1"):
        return -1
    lists[0]=source[0][0]
    lists[1]=source[0][1]
    for i in source[1:]:
        if(i[0] in lists):
            for x in range(len(lists)):
                if(lists[x]==i[0]):
                    if(lists[2*x+1]=="*"):
                        lists[2*x+1]=i[1]
                    else:
                        lists[2*x+2]=i[1]
        elif(i[1] in lists):
            y=i[1]
            i[1]=i[0]
            i[0]=y
            for x in range(len(lists)):
                if(lists[x]==i[0]):
                        if(lists[2*x+1]=="*"):
                            lists[2*x+1]=i[1]
                        else:
                            lists[2*x+2]=i[1]
        else:
            return -1
    sum=0
    for i in range(len(sources)):
        sum=sum+int(sources[i][2])
    return sum
n_m=input().split()
n=int(n_m[0])
m=int(n_m[1])
source=[]
res=[]
try:
    while(True):
        x=input().split()
        source.append(x)
except(EOFError):
    pass
lists=list(combinations(source,m))
for i in lists:
    res.append(create_tree(i))
print(max(res))