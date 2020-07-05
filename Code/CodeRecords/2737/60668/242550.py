def arrays_13_mostNum(list = []):
    list_0 = []
    for item in list:
        if item not in list_0:
            list_0.append(item)
    list_1 = []
    n = int(len(list)/3)
    co = 0
    for item in list_0:
        for i in range(0,len(list)):
            if list[i]==item:
                co+=1
            if co>n:
                list_1.append(item)
        co = 0
    list_re = []
    for ie in list_1:
        if ie not in list_re:
            list_re.append(ie)
    print(list_re)
if __name__ =='__main__':
    list = eval(input())
    arrays_13_mostNum(list)
