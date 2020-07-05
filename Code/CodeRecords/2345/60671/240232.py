time=int(input())
while(time>0):
    length=int(input())
    str1=input()
    list1=str1.split()
    listNum=[]
    for x in list1:
        listNum.append(int(x))
    listNum.sort()
    lack=0
    more=0
    for i in range(length):
        if(listNum[i]!=i+1):
            lack=i+1
            more=listNum[i]
            break
    print(more,lack)
    time-=1