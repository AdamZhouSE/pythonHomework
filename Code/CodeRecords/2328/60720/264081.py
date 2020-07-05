list0=input().split(',')
list0=[int(list0[i]) for i in range(len(list0))]
list0.sort()
str1=''
if list0[1]>=6 or list0[0]>2:
    print(str1,end='')
else:
    index=-1
    max=0
    for i in range(len(list0)):
        if list0[i]<=2:
            if list0[i]>max:
                max=list0[i]
                index=i
    str1=str(max)
    del list0[index]
    index = -1
    max = 0
    if str1=='2':
        for i in range(len(list0)):
            if list0[i] < 4:
                if list0[i] > max:
                    max = list0[i]
                    index = i
        str1=str1+str(list0[index])+':'
        del list0[index]
    else:
        str1 = str1 + str(list0[-1]) + ':'
        del list0[-1]
    if list0[1]<6:
        str1=str1+str(list0[1])+str(list0[0])
    else:
        str1=str1+str(list0[0])+str(list0[1])
    print(str1)