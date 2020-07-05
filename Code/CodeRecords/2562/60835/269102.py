n = int(input())
for x in range(n):
    tem = input().split(' ')
    N = int(tem[0])
    Q = int(tem[1])
    tem = input().split(' ')
    operation = []
    for h in tem:
        operation.append(int(h))
    unread = []
    read = []
    trash = []
    for h in range(1,N+1):
        unread.append(h)
    for h in range(Q):
        index = 2*h
        if operation[index] == 1:
            unread.remove(operation[index+1])
            read.append(operation[index+1])
        elif operation[index] == 2:
            read.remove(operation[index+1])
            trash.append(operation[index+1])
        elif operation[index] == 3:
            unread.remove(operation[index+1])
            trash.append(operation[index+1])
        elif operation[index] == 4:
            trash.remove(operation[index+1])
            read.append(operation[index+1])
    for h in unread:
        print(h,end=" ")
    print()
    for h in read:
        print(h,end=" ")
    print()
    for h in trash:
        print(h,end=" ")
    print()
    