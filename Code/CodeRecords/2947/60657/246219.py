num=input()
ori=input()
opr=[]
for i in range(int(num)):
    a=input().split(' ')
    opr.append(a)
cons=[]
for i in range(len(opr)):
    if opr[i][0]=='1':
        cons.append(ori+opr[i][1])
        ori=ori+opr[i][1]
    elif opr[i][0]=='2':
        ori=ori[int(opr[i][1]):(int(opr[i][1])+int(opr[i][2]))]
        cons.append(ori)
    elif opr[i][0] == '3':
        temp=[]
        for k in ori:
            temp.append(k)
        temp.insert(int(opr[i][1]),opr[i][2])
        temp=''.join(temp)
        cons.append(temp)
        ori=temp

    elif opr[i][0] == '4':
        temp = []
        for k in ori:
            temp.append(k)
        temp=''.join(temp)
        cons.append(temp.index(opr[i][1]))
for i in cons:
    print(i)
