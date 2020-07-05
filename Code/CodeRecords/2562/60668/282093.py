def linerlist_1_mail(N, req=[]):
    N_id = [int(i) for i in range(1, N + 1)]
    do_list = [req[i] for i in range(0, len(req), 2)]
    Id = [req[i] for i in range(1, len(req), 2)]
    UNREAD = N_id
    READ = []
    TRASH = []
    for i in range(len(do_list)):
        if do_list[i] == 1:
            READ.append(Id[i])
            del UNREAD[UNREAD.index(Id[i])]
        elif do_list[i] == 2:
            TRASH.append(Id[i])
            del READ[READ.index(Id[i])]
        elif do_list[i] == 3:
            TRASH.append(Id[i])
            del UNREAD[UNREAD.index(Id[i])]
        elif do_list[i] == 4:
            READ.append(Id[i])
            del TRASH[TRASH.index(Id[i])]
    if len(UNREAD)==0:
        print("EMPTY")
    else:
        for i in range(len(UNREAD)-1):
            print(UNREAD[i],end=' ')
    print(UNREAD[len(UNREAD)-1],end=' \n')
    if len(READ) == 0:
        print("EMPTY")
    else:
        for i in range(len(READ)-1):
            print(READ[i], end=' ')
    print(READ[len(READ)-1],end=' \n')
    if len(TRASH) == 0:
        print("EMPTY")
    else:
        for i in range(len(TRASH)-1):
            print(TRASH[i], end=' ')
    print(TRASH[len(TRASH)-1],end=' \n')
if __name__ == '__main__':
    for _ in range(int(input())):
        N, Q = input().split()
        N = int(N)
        req = [int(i) for i in input().split()]
        linerlist_1_mail(N, req)



