def arrays_14_bigestSquare(list = []):
    maxF = 0
    list_new = []
    for i in range(0,len(list)):  #行
        list_1 = []
        co = 0
        for j in range(0,len(list[i])): #列
            if list[i][j]!='0':
                co += 1
                list_1.append(co)
            else:
                co=0
                list_1.append(co)
        list_new.append(list_1)
    for i in range(0,len(list_new)):
        for j in range(0,len(list_new[i])):
            minNum = list_new[i][j]
            for i_u in range(i,0,-1):
                height = i - i_u + 1
                minNum = min(minNum,list_new[i_u][j])
                maxF = max(maxF,height*minNum)
    print(maxF)
if __name__ =='__main__':
    list_0 = []
    list_new = []
    n = 100
    while n>0:
        m = input().replace(' ','')
        if m == ']':
            break
        elif m != '[':
            list_0.append(m)
    for i in range(0,len(list_0)-1):
        list_new.append(eval(list_0[i][:-1]))
    list_new.append(eval(list_0[len(list_0)-1]))
    arrays_14_bigestSquare(list_new)