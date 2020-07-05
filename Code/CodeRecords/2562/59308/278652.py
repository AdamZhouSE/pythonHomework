import re
pattern = re.compile('[0-9]+')

t = int(input())
for _ in range(t):
    a = pattern.findall(input())
    n, q = int(a[0]), int(a[1])
    unread = [i for i in range(1, n+1)]
    read = list()
    trash = list()
    a = [int(x) for x in pattern.findall(input())]
    for i in range(0, len(a), 2):
        x = a[i]
        y = a[i+1]
        if x == 1:
            unread.remove(y)
            read.append(y)
        if x == 2:
            read.remove(y)
            trash.append(y)
        if x == 3:
            unread.remove(y)
            trash.append(y)
        if x == 4:
            trash.remove(y)
            read.append(y)
    if len(unread) == 0:
        print("EMPTY")
    else:
        print(*unread, end=' \n')
    if len(read) == 0:
        print("EMPTY")
    else:
        print(*read, end=' \n')
    if len(trash) == 0:
        print("EMPTY")
    else:
        print(*trash, end=' \n')


