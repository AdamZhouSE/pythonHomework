n=int(input())
for i in range(n):
    listt=input().split()
    a=int(listt[0])
    q=int(listt[1])
    list=input().split()
    list1=[] #unread
    list2=[] #read
    list3=[] #trash
    for j in range(a):
        list1.append(j+1)
    for j in range(0,2*q,2):
        c=int(list[j])
        d=int(list[j+1])
        if c==1:
            e=list1.index(d)
            list2.append(d)
            del list1[e]
        elif c==2:
            e = list2.index(d)
            list3.append(d)
            del list2[e]
        elif c==3:
            e = list1.index(d)
            list3.append(d)
            del list1[e]
        else:
            e = list3.index(d)
            list2.append(d)
            del list3[e]
    if len(list1)==0:
        print('EMPTY')
    else:
        for j in range(len(list1)-1):
            print(list1[j],end=' ')
        print(list1[-1],end='')
        print(' ')
    if len(list2) == 0:
        print('EMPTY')
    else:
        for j in range(len(list2) - 1):
            print(list2[j], end=' ')
        print(list2[-1], end='')
        print(' ')
    if len(list3)==0:
        print('EMPTY')
    else:
        for j in range(len(list3) - 1):
            print(list3[j], end=' ')
        print(list3[-1], end='')
        print(' ')