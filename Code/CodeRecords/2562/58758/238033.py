count = int(input())
for i in range(0, count):
    num, step = input().split()
    UNREAD = []
    READ = []
    TRASH = []
    for j in range(0, int(num)):
        UNREAD.append(j+1)
    codes = input().split()
    for k in range(0, int(step)):
        code = int(codes[2*k])
        message = int(codes[2*k+1])
        if code == 1:
            UNREAD.remove(message)
            READ.append(message)
        elif code == 2:
            READ.remove(message)
            TRASH.append(message)
        elif code == 3:
            UNREAD.remove(message)
            TRASH.append(message)
        else:
            TRASH.remove(message)
            READ.append(message)
    if len(UNREAD) == 0:
        print('EMPTY')
    else:
        for m in UNREAD:
            print(m, end=' ')
        print()
    if len(READ) == 0:
        print('EMPTY')
    else:
        for m in READ:
            print(m, end=' ')
        print()
    if len(TRASH) == 0:
        print('EMPTY')
    else:
        for m in TRASH:
            print(m, end=' ')
        print()
