T = int(input())

for k in range(0, T):
    temp1 = list(input().split(" "))
    N = int(temp1[0])
    Q = int(temp1[1])
    temp = list(input().split(" "))
    lists = []
    oper=[]
    operNum=[]

    for x in temp:
        lists.append(int(x))

    # 初始化
    unread=[]
    read=[]
    trash=[]
    for i in range(1,N+1):
        unread.append(i)

    i=0
    while i<Q:
        oper.append(lists[2*i])
        operNum.append(lists[2*i+1])
        i=i+1

    while len(oper)!=0:
        if oper[0]==1:
            unread.remove(operNum[0])
            read.append(operNum[0])
        if oper[0]==2:
            read.remove(operNum[0])
            trash.append(operNum[0])
        if oper[0]==3:
            unread.remove(operNum[0])
            trash.append(operNum[0])
        if oper[0]==4:
            trash.remove(operNum[0])
            read.append(operNum[0])
        oper.remove(oper[0])
        operNum.remove(operNum[0])

    if len(unread)!=0:
        for x in unread:
            print(str(x)+" ",end="")
        print()
    else:
        print("EMPTY")

    if len(read)!=0:
        for x in read:
            print(str(x)+" ",end="")
        print()
    else:
        print("EMPTY")

    if len(trash)!=0:
        for x in trash:
            print(str(x)+" ",end="")
        print()
    else:
        print("EMPTY")
