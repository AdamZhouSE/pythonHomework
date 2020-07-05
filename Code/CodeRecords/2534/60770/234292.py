def solve():
    give = input()
    lists = []
    lists = give.split('[')
    lists[3] += ','
    give = ''
    for list in lists:
        list += '['
        give += list
    give = give[:-1]
    pointer=[]
    total=0
    res=[]
    strl=give.split('[')
    strl=strl[2:]
    for i in range(len(strl)):
        strl[i]=strl[i][:-2]
    
    lists=[]
    for strs1 in strl:
        strs1=strs1[::-1]
        temp=strs1.split(',')
        for i in range(len(temp)):
            temp[i]=int(temp[i])
        lists.append(temp)
        pointer.append(len(temp)-1)
        total+=len(temp)

    
    while total>0:
        index=-1
        min=255
        for i in range(len(lists)):
            current=lists[i][pointer[i]]
            if current<min:
                min=current
                index=i
        res.append(min)
        pointer[index]-=1
        if pointer[index]<0:
            del lists[index]
            del pointer[index]
        total-=1

    print(res)




if __name__=='__main__':
    solve()
