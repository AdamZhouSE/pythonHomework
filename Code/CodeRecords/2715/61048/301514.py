def search6():
    set=[]
    str = list(input()[2 : - 2].split('],['))
    for i in range(len(str)):
        arr=[int(x) for x in str[i].split(',')]
        set.append(arr)
    parent=[int(x) for x in range(len(set))]
    res=len(set)
    for i in range(len(set)):
        for j in range(len(set)):
            if(i!=j and (set[i][0]==set[j][0] or set[i][1]==set[j][1])):

                x1=find(i,parent)
                x2=find(j,parent)
                if(x1!=x2):
                    parent[x2]=x1
                    res-=1
    print(len(set)-res)
    return


def find(x,parent):
    if parent[x]==x:
        return x
    else:
        return find(parent[x],parent)

search6()