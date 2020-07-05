T = int(input())
for ttt in range(T):
    input()
    aList = sorted([int(i) for i in input().strip().split(' ')])
    diction = {}
    for i in aList:
        if i in diction:
            diction[i] = 2
        else:
            diction[i] = 1
    k = int(input())
    res = 0
    if k == 0:
        for i in diction.items():
            if i[1] == 2:
                res += 1
    else:
        for i in diction.keys():
            if k+i in diction.keys():
                res += 1
    print(res)