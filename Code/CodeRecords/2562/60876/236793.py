import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    N,Q=map(int,sys.stdin.readline().split())
    unread=[]
    read=[]
    trash=[]
    for j in range(0,N):
        unread.append(j+1)
    t=sys.stdin.readline().split()
    for j in range(0,Q):
        m=int(t[2*j])
        num=int(t[2*j+1])
        if m==1:
            temp=unread.index(num)
            del unread[temp]
            read.append(num)
        elif m==2:
            temp=read.index(num)
            del read[temp]
            trash.append(num)
        elif m==3:
            temp=unread.index(num)
            del unread[temp]
            trash.append(num)
        else:
            temp=trash.index(num)
            del trash[temp]
            read.append(num)
    if len(unread)!=0:
        for item in unread:
            print(item,end=' ')
    else:
        print(" EMPTY")
    print()
    if len(read)!=0:
        for item in read:
            print(item,end=' ')
    else:
        print(" EMPTY")
    print()
    if(len(trash)!=0):
        for item in trash:
            print(item,end=" ")
    else:
        print(" EMPTY")
    print()