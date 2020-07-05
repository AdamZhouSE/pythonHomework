def sort10():
    set=[]
    str = list(input()[2: - 2].split('],['))
    for i in range(len(str)):
        arr=[int(x) for x in str[i].split(',')]
        set.append(arr)
    veganF=int(input())
    maxPrice=int(input())
    maxDistance=int(input())

    res=[]
    picked=[]
    '''for row in set:
        if(veganF==1 and row[2]==0):
            set.remove(row)
            continue
        if(maxPrice<row[3] or maxDistance<row[4]):
            set.remove(row)
            continue'''
    for i in range(len(set)):
        if((not (veganF==1 and set[i][2]==0))and maxPrice>=set[i][3] and maxDistance>=set[i][4]):
            picked.append(set[i])
    '''for i in range(len(set)):
        for j in range(len(set)-1):
            if set[j][1]<set[j+1][1]:
                temp=set[j]
                set[j]=set[j+1]
                set[j+1]=temp
            if set[j][1]==set[j+1][1] and set[j][0]<set[j+1][0]:
                temp = set[j]
                set[j] = set[j + 1]
                set[j + 1] = temp
    for row in set:
        res.append(row[0])'''
    for i in range(len(picked)):
        for j in range(len(picked)-1):
            if picked[j][1]<picked[j+1][1]:
                temp=picked[j]
                picked[j]=picked[j+1]
                picked[j+1]=temp
            if picked[j][1]==picked[j+1][1] and picked[j][0]<picked[j+1][0]:
                temp = picked[j]
                picked[j] = picked[j + 1]
                picked[j + 1] = temp
    for row in picked:
        res.append(row[0])
    print(res)
    return



sort10()