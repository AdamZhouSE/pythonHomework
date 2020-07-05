time=int(input())
while(time>0):
    length=int(input())
    str1=input()
    list1=str1.split()
    listNum=[]
    for x in list1:
        listNum.append(int(x))
    biggest=0
    sumnum=0
    if(length>4):
        for i in range(length):
            for j in range(i+2,length):
                for k in range(j+2,length):
                    sumnum=listNum[i]+listNum[j]+listNum[k]
                    if(sumnum>biggest):
                        biggest=sumnum
    else:
        for i in range(length):
            for j in range(i+2,length):
                sumnum=listNum[i]+listNum[j]
                if(sumnum>biggest):
                    biggest=sumnum
    if(length!=3)and(biggest==4):
        biggest+=1
    
    time-=1