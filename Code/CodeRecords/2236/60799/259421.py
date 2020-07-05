n = int(input())  # 都用py了还考虑什么效率
nList = []
for ttt in range(n):
    L = input().strip().split()
    op = int(L[0])
    x = int(L[1])
    if op == 1:
        nList.append(x)
        nList.sort()
    elif op == 2:
        nList.remove(x)
    elif op == 3:
        print(nList.index(x) + 1)
    elif op == 4:
        print(nList[x - 1])
    else:
        left = right = -1
        for i in range(len(nList)):
            if nList[i] < x:
                left = i
            if nList[i] > x:
                right = i
                break
        if op == 5:
            print(nList[left])
        else:
            print(nList[right])
