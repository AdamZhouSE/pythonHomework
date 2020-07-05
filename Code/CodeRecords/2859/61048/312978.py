def arr4():
    num=int(input())
    set=[]
    res=True
    for i in range(num):
        set.append([x for x in input()])
    fst=set[0][0]
    ots=set[0][1]
    for i in range(num):
        if not (set[i][i]==fst and set[i][num-1-i]==fst):
            res=False
    for i in range(num):
        for j in range(num):
            if (i!=j and i+j!=num-1):
                if(set[i][j]!=ots):
                    res=False
    if(fst==ots):
        res=False
    print("YES") if res==True else print("NO")
    return

arr4()