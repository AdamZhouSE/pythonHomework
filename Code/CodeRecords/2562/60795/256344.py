T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    n=arr[0]
    q=arr[1]
    cmd=[int(n) for n in input().split(' ')]
    k,read,trash,unread=0,[],[],[]
    for j in range(0,n):
        unread.append(j+1)
    while k<2*q:
        if cmd[k]==1:
            read.append(cmd[k+1])
            unread.remove(cmd[k+1])
        elif cmd[k]==2:
            trash.append(cmd[k+1])
            read.remove(cmd[k+1])
        elif cmd[k]==3:
            trash.append(cmd[k+1])
            unread.remove(cmd[k + 1])
        elif cmd[k]==4:
            read.append(cmd[k + 1])
            trash.remove(cmd[k+1])
        k=k+2
    if len(unread)==0:
        print("EMPTY")
    else:
        for j in range(0,len(unread)):
            print(unread[j],end=" ")
        print("")
    if len(read)==0:
        print("EMPTY")
    else:
        for j in range(0,len(read)):
            print(read[j],end=" ")
        print("")
    if len(trash)==0:
        print("EMPTY")
    else:
        for j in range(0,len(trash)):
            print(trash[j],end=" ")
        print("")