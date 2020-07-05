def printAsRequired(list):
    for i in list:
        print(i,'',end='')
    print()

k=int(input())
while k:
    line=[int(x) for x in input().split()]
    n=line[0]
    q=line[1]
    unread=[]
    read=[]
    trash=[]
    for i in range(n+1):
        unread.append(i)
    instr=[int(x) for x in input().split()]
    for i in range(q):
        qNO=instr[2*i]
        mailNO=instr[2*i+1]
        if qNO==1:
            unread.remove(mailNO)
            read.append(mailNO)
        elif qNO==2:
            read.remove(mailNO)
            trash.append(mailNO)
        elif qNO==3:
            unread.remove(mailNO)
            trash.append(mailNO)
        else: #instr[i]==4
            trash.remove(mailNO)
            read.append(mailNO)
    del unread[0]
    printAsRequired(unread)
    printAsRequired(read)
    printAsRequired(trash)
    k-=1