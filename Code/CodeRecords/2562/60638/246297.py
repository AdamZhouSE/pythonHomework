num = int(input())
for x in range(0,num):
    list1=list(map(int, input().split(" ")))
    list2=list(map(int, input().split(" ")))
    unread=list(range(1,list1[0]+1))
    read=[]
    trash=[]
    for i in range(0,len(list2)):
        if i%2==0:
            if list2[i]==1:
                unread.remove(list2[i+1])
                read.append(list2[i+1])
            elif list2[i]==2:
                read.remove(list2[i + 1])
                trash.append(list2[i + 1])
            elif list2[i]==3:
                unread.remove(list2[i + 1])
                trash.append(list2[i + 1])
            elif list2[i]==4:
                trash.remove(list2[i + 1])
                read.append(list2[i + 1])
    a=False
    b=False
    c=False
    for j in unread:
        a=True
        print(j,end=" ")
    if not a:
        print("EMPTY")
    print()
    for j in read:
        b = True
        print(j, end=" ")
    if not b:
        print("EMPTY")
    print()
    for j in trash:
        c = True
        print(j, end=" ")
    if not c:
        print("EMPTY")
    print()