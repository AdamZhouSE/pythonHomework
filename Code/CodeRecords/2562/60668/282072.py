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
    for item in N_id:
        if (item not in READ) and (item not in TRASH):
            UNREAD.append(item)
    UNREAD.sort()
    READ.sort()
    TRASH.sort()
    pr(UNREAD)
    pr(READ)
    pr(TRASH)
def pr(list=[]):
    if len(list) == 0:
        print("EMPTY")
    else:
        for i in range(len(list) - 1):
            print(list[i], end=' ')
        print(list[len(list) - 1])
if __name__ == '__main__':
    for _ in range(int(input())):
        N, Q = input().split()
        N = int(N)
        req = [int(i) for i in input().split()]
        linerlist_1_mail(N, req)


