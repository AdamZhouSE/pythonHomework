time=int(input())
while(time>0):
    str0=input()
    len1=int(str0[0])
    len2=int(str0[2])
    str1=input()
    str2=input()
    list1=str1.split()
    list2=str2.split()
    listnum1=[]
    listnum2=[]
    for x in list1:
        listnum1.append(int(x))
    for x in list2:
        listnum2.append(int(x))
    newlist=listnum1+listnum2
    newlist.sort()
    print(*newlist,end=" ")
    print()
    time-=1