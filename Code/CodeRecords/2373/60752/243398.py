num=int(input())
for i in range(num):
    size=int(input())
    eles=list(map(int,input().split(' ')))
    tosort=eles.copy()
    index=[]
    for a in range(size):
        index.append(a)
    sortedEles_index=list(zip(tosort,index))
    sortedEles_index.sort(key=lambda x:x[0],reverse=True)
    sum=0
    list_stolen_eles_index=[]
    for a in range(size):
        list_stolen_eles_index.append([eles[a],False,sortedEles_index[a][0],sortedEles_index[a][1]])
    for h in range(size):
        money=list_stolen_eles_index[h][2]
        idx=list_stolen_eles_index[h][3]
        if list_stolen_eles_index[idx][1] :
            continue
        if h+2<size:
            money1=list_stolen_eles_index[h+1][2]
            id1=list_stolen_eles_index[h+1][3]
            money2=list_stolen_eles_index[h+2][2]
            id2=list_stolen_eles_index[h+2][3]
            if money1+money2>money and ((id1+1==idx and id2-1==idx)or(id1-1==idx and id2+1==idx)):
                sum=sum+money1+money2
                list_stolen_eles_index[id1][1]=True
                list_stolen_eles_index[id2][1]=True
                continue
        if 0<idx<size-1:
            neighbor1=idx-1
            neighbor2=idx+1
            if list_stolen_eles_index[neighbor1][1] is False and list_stolen_eles_index[neighbor2][1] is False:
                sum+=money
                list_stolen_eles_index[idx][1]=True
        if idx==0:
            if list_stolen_eles_index[1][1] is False:
                sum+=money
                list_stolen_eles_index[0][1]=True
        if idx==size-1:
            if list_stolen_eles_index[size-2][1] is False:
                sum+=money
                list_stolen_eles_index[size-1][1]=True
    print(sum)


