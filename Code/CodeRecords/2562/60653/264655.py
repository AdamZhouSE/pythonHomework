m = int(input())
for v in range(0, m):
    n, q = map(int, input().split())
    ls = list(int(o) for o in input().split())
    UNREAD = list(int(a) for a in range(1, n+1))
    READ = []
    TRASH = []
    for i in range(0, q*2, 2):
        if ls[i] == 1:
            READ.append(ls[i+1])
            UNREAD.remove(ls[i + 1])
        elif ls[i] == 2:
            TRASH.append(ls[i+1])
            READ.remove(ls[i+1])
        elif ls[i] == 3:
            TRASH.append(ls[i + 1])
            UNREAD.remove(ls[i + 1])
        else:
            READ.append(ls[i + 1])
            TRASH.remove(ls[i + 1])
    for i in UNREAD:
        print(i, end=' ')
    print('')
    for i in READ:
        print(i, end=' ')
    print('')
    for i in TRASH:
        print(i, end=' ')
    print('')