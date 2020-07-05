def up(List,x):
    newlist=[]
    if len(List)==0:
        return 1
    for i in range(len(List)):
        if List[i]>x:
            for j in range(i+1,len(List)):
                newlist.append(List[j])
            return 1+up(newlist,List[i])
    return 1

def Up(List):
    Max=0
    for i in range(len(List)):
        if up(List[i:len(List)],List[i])>Max:
            Max=up(List[i:len(List)],List[i])
    return Max

List=list(map(int,input().split(',')))
print(Up(List))