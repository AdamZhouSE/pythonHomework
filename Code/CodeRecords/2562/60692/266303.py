nums = int(input())
for i in range(nums):
    unread = []
    read = []
    trash = []
    n_q = input().split(" ")
    n = int(n_q[0])
    q = int(n_q[1])
    list1 = input().split(" ")
    for m in range(1, n + 1):
        unread.append(str(m))
    for j in range(0, 2 * q, 2):
        if list1[j] == '1':
            unread.remove(list1[j + 1])
            read.append(list1[j + 1])
        elif list1[j] == '2':
            read.remove(list1[j + 1])
            trash.append(list1[j + 1])
        elif list1[j] == '3':
            unread.remove(list1[j + 1])
            trash.append(list1[j + 1])
        elif list1[j] == '4':
            trash.remove(list1[j + 1])
            read.append(list1[j + 1])
    if not unread:
        print("EMPTY")
    else:
        print(" ".join(unread))
    if not read:
        print("EMPTY")
    else:
        print(" ".join(read))
    if not trash:
        print("EMPTY")
    else:
        print(" ".join(trash))
