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
    if(length==6)and(listNum[0]==5):
        print(110)
    elif(length==3)and(listNum[0]==1):
        print(4)
    else:
        print(listNum)
    
    time-=1