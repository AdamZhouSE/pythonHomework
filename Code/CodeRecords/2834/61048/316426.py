def arr38():
    line1 = input().split(' ')
    n, m = int(line1[0]), int(line1[1])
    set=[]
    res=0
    for i in range(n):
        set.append([x for x in input()])

    socres=[int(x) for x in input().split(' ')]
    for i in range(m):
        map={}
        for j in range(n):
            if(set[j][i] in map):
                map[set[j][i]]+=1
            else:
                map[set[j][i]]=1
        tmp=sorted(map.values())

        res+=tmp[-1]*socres[i]
    print(res)
    return

arr38()