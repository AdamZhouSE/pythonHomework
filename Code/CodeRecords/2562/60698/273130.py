def test():
    t=int(input())
    nq=input().split()
    n=int(nq[0])
    q=int(nq[1])
    unread=[i+1 for i in range(0,n)]
    read=[]
    trash=[]
    quarys=input().split()
    quarys=list(map(int,quarys))
    for i in range(0,q):
        oper=quarys[i*2]
        mid=quarys[2*i+1]
        if oper==1:
            unread.remove(mid)
            read.append(mid)
        elif oper==2:
            read.remove(mid)
            trash.append(mid)
        elif oper==3:
            unread.remove(mid)
            trash.append(mid)
        elif oper==4:
            trash.remove(mid)
            read.append(mid)
    p(unread)
    p(read)
    p(trash)
def p(lis):
    if len(lis)==0:
        print("EMPTY")
    else:
        print(' '.join(list(map(str,lis)))+' ')
test()