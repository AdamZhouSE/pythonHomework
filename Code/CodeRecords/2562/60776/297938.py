a=int(input())
for k in range(0,a):
    n=int(input().split(' ')[0])
    b=input().split(' ')
    for i in range(0,len(b)):
        b[i]=int(b[i])
    unread=[]
    for i in range(1,n+1):
        unread.append(i)
    read=[]
    trash=[]
    for i in range(0,int(len(b)/2)):
        if b[i*2]==1:
            read.append(b[i*2+1])
            unread.remove(b[2*i+1])
        elif b[i*2]==2:
            trash.append(b[i*2+1])
            read.remove(b[2*i+1])
        elif b[i*2]==3:
            trash.append(b[i*2+1])
            unread.remove(b[2*i+1])
        else:
            read.append(b[i * 2 + 1])
            trash.remove(b[2 * i + 1])
    if unread==[]:
        print("EMPTY")
    else:
        print(" ".join(str(i) for i in unread),end=" ")
        print()
    if read==[]:
        print("EMPTY")
    else:
        print(" ".join(str(i) for i in read),end=" ")
        print()
    if trash==[]:
        print("EMPTY")
    else:
        print(" ".join(str(i) for i in trash),end=" ")
        print()