def mail():
    row1=input().split(" ")
    N=int(row1[0])
    Q=int(row1[1])
    deal=input().split(" ")
    unread=[]
    read=[]
    trash=[]
    for i in range(1,N+1):
        unread.append(i)
    idx=0
    for q in range(0,Q):
        op=deal[idx]
        tar=deal[idx+1]
        if op==1:
            unread.remove(tar)
            read.append(tar)
        elif op==2:
            read.remove(tar)
            trash.append(tar)
        elif op==3:
            unread.remove(tar)
            trash.append(tar)
        elif op==4:
            trash.remove(tar)
            read.append(tar)
    if not unread:
        print("EMPTY")
    else:
        for idx in unread:
            print(idx+" ")
    if not read:
        print("EMPTY")
    else:
        for idx in read:
            print(idx + " ")
    if not trash:
        print("EMPTY")
    else:
        for idx in trash:
            print(idx+" ")
            
if __name__=='__main__':
    mail()