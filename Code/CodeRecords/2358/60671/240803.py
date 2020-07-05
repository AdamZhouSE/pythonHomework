time=int(input())
while(time>0):
    str1=input()
    length=int(str1[0])
    take=int(str1[2])
    str2=input()
    list=str2.split()
    listNum=[]
    for x in list:
        listNum.append(int(x))
    listNum.sort()
    listNum.reverse()
    listNew=listNum[:take]
    print(*listNew,end=" ")
    print()
    time-=1