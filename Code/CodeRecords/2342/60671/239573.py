time=int(input())
while(time>0):
    str1=input()
    length=int(str1[0])
    num=int(str1[2])
    str2=input()
    list1=str2.split()
    listNum=[]
    for x in list1:
        listNum.append(int(x))
    listNum.sort()
    listN1=listNum[:num]
    listN1.reverse()
    listN2=listNum[num:]
    endList=listN1+listN2
    print(*endList)
    time-=1