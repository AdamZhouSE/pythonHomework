moves=eval(input())
def isWin(flag):
    for j in range(2):
        hash1 = {}
        for i in range(flag, len(moves), 2):
            hash1[moves[i][j]] = hash1.get(moves[i][j], 0) + 1
        if max(hash1.values()) >= 3:
            return True
    win_set1 = ((0, 0), (1, 1), (2, 2))
    win_set2 = ((2, 0), (0, 2), (1, 1))
    count1 = 0
    count2 = 0
    for k in range(flag, len(moves), 2):
        if tuple(moves[k]) in win_set1:
            count1 += 1
        if tuple(moves[k]) in win_set2:
            count2 += 1
    count = count1 if count1 > count2 else count2
    # for m in range(1):
    #     for n in range(flag,len(moves),2):
    #         _is = moves[n][m]
    #         if moves[n][m+1] == _is*moves[n][m+1]/2:
    #             count += 1
    if count >= 3:
        return True
    return False


if not moves or len(moves) < 5:
    print('Pending')
elif 5 <= len(moves) <= 9:
    if isWin(0):
        print('A')
    elif isWin(1):
        print('B')
    elif not isWin(1) and not isWin(0) and len(moves) < 9:
        print('Pending')
    else:
        print('Draw')