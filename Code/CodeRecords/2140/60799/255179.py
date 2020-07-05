T = int(input())
for ttt in range(T):
    n = int(input())
    nList = [i for i in range(n)]
    ptr = 0
    resList = [-1] * n
    for i in range(1, n + 1):
        for j in range(i):
            ptr += 1
            if ptr == len(nList):
                ptr = 0
        resList[nList.pop(ptr)] = str(i)  # 没有链表么
        if ptr == len(nList):
            ptr = 0
    print(' '.join(resList))