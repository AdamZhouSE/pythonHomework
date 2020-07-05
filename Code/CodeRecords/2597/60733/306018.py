lists = list()
prices = list()
notes = list()
while True:
    strs = input().split()
    notes.append(strs)
    opera = [int(i) for i in strs]
    if opera[0]==1:
        check = True
        for j in range(len(lists)):
            if lists[j][1]==opera[2]:
                check=False
        if check:
            temp = list()
            temp.append(opera[1])
            temp.append(opera[2])
            prices.append(opera[2])
            lists.append(temp)
    elif opera[0]==3:
        if len(lists)==0:
            continue
        pricelow = []
        temp1 = min(prices)
        for j in range(len(lists)):
            if lists[j][1]==temp1:
                pricelow = lists[j]
                break
        lists.remove(pricelow)
    elif opera[0]==2:
        if len(lists)==0:
            continue
        pricehigh = []
        temp2 = max(prices)
        for j in range(len(lists)):
            if lists[j][1]==temp2:
                pricehigh = lists[j]
        lists.remove(pricehigh)
    elif opera[0]==-1:
        index1 = 0
        index2 = 0
        for j in range(len(lists)):
            index1+=lists[j][0]
            index2+=lists[j][1]
        if index1==6 and index2==9:
           print(notes) 
        print("{} {}".format(index1,index2),end='')
        break