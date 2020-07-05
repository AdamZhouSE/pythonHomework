def nums_19_sameMinus(list = []):
    co = 0
    coun = 0
    diffe = []
    list_0 = []
    list = sorted(list)
    for i in range(len(list)-1):
        diff = list[i+1]-list[i]
        if diff not in diffe:
            for j in range(i+1,len(list)-1):
                if list[j+1] - list[j] ==diff:
                    if list[j+1] not in list_0:
                        list_0.append(list[j+1])
                    if list[j] not in list_0:
                        list_0.append(list[j])
            coun += pow(2,len(list_0)) - 1
            diffe.append(diff)
            list_0 = []
    print(coun)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_19_sameMinus(list)