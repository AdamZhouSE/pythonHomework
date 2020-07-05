numOfInput = int(input())
for i in range(numOfInput):
    NQ = input().split(" ")
    N = int(NQ[0])
    Q = int(NQ[1])
    options = input().split(" ")
    options = list(map(int,options))
    unread = []
    read = []
    trash = []
    for j in range(1,N+1):
        unread.append(j)
    for j in range(Q):
        opt = options[2*j]
        mail = options[2*j+1]
        if opt == 1:
            unread.remove(mail)
            read.append(mail)
        elif opt == 2:
            read.remove(mail)
            trash.append(mail)
        elif opt == 3:
            unread.remove(mail)
            trash.append(mail)
        else:
            trash.remove(mail)
            read.append(mail)
    for j in unread:
        print(j,end = " ")
    print("")
    for j in read:
        print(j,end = " ")
    print("")
    for j in trash:
        print(j,end = " ")
    print("")