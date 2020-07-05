arr=input().split(' ')
num,root=int(arr[0]),int(arr[1])
list=[]
for i in range(0,num):
    at=[int(n) for n in input().split(' ')]
    list.append(at)
count=num
lch,rch,wrong=[],[],[]
for i in range(0,num):
    if list[i][0]==root:
        if list[i][1]<root:
            if list[i][1]!=0:
                lch.append(list[i][1])
        else:
            count=count-1
            wrong.append(list[i][1])
        if list[i][2]>root:
            rch.append(list[i][2])
        else:
            if list[i][2]!=0:
                count=count-1
                wrong.append(list[i][2])
    else:
        if list[i][0] in wrong:
            if list[i][1]!=0:
                count=count-1
            if list[i][2]!=0:
                count=count-1
        elif list[i][0] in lch:
            if list[i][1]<list[i][0]:
                if list[i][1]!=0:
                    lch.append(list[i][1])
            else:
                count=count-1
                wrong.append(list[i][1])
            if list[i][2]>list[i][0]:
                lch.append(list[i][2])
            else:
                if list[i][2]!=0:
                    count=count-1
                    wrong.append(list[i][2])
        elif list[i][0] in rch:
            if list[i][1]<list[i][0]:
                if list[i][1]!=0:
                    rch.append(list[i][1])
            else:
                count=count-1
                wrong.append(list[i][1])
            if list[i][2]>list[i][0]:
                rch.append(list[i][2])
            else:
                if list[i][2]!=0:
                    count=count-1
                    wrong.append(list[i][2])
print(count)
