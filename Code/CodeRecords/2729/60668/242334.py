def arrays_11_numFind(list = []):
    list_0 = []
    for item in list:
        if item not in list_0:
            list_0.append(item)
    co = [0 for x in range(0,len(list_0))]
    i =0
    for ite in list_0:
        for it in list:
            if ite == it:
                co[i] += 1
        i += 1
    for i in range(0,len(list_0)):
        if co[i] ==1:
            print(list_0[i])
if __name__ =='__main__':
    list = eval(input())
    arrays_11_numFind(list)