t=eval(input())
for _ in range(t):
    num=list(map(int,input().strip().split(' ')))
    n=num[0]
    q=num[1]
    UNREAD=[i+1 for i in range(n)]
    READ=[]
    TRASH=[]
    option=list(map(int,input().strip().split(' ')))
    for i in range(q):
        temp=option[2*i+1]
        if option[2*i]==1:
            UNREAD.remove(temp)
            READ.append(temp)
        elif option[2*i]==2:
            READ.remove(temp)
            TRASH.append(temp)
        elif option[2*i]==3:
            UNREAD.remove(temp)
            TRASH.append(temp)
        elif option[2*i]==4:
            TRASH.remove(temp)
            READ.append(temp)
    if len(UNREAD)==0:
        print('EMPTY')
    else:
        for i in UNREAD:
            print(i,end=' ')
        print()
    if len(READ)==0:
        print('EMPTY')
    else:
        for i in READ:
            print(i,end=' ')
        print()
    if len(TRASH)==0:
        print('EMPTY')
    else:
        for i in TRASH:
            print(i,end=' ')
        print()
            