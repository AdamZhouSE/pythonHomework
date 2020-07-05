def largestComponentSize(A):
    if len(A) <= 1:
        return len(A)
    cal = []
    flagp = {}
    flaga = [-1 for i in range(len(A))]
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
             227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
             349, 353, 359]
    for i in range(len(A)):
        cal.append(plist(A, i, prime))
    for i in range(len(cal)):
        flaga[i] = -1
        for j in range(len(cal[i])):
            keyp = flagp.get(cal[i][j], -1)
            if flaga[i] == -1:
                flaga[i] = flagp.get(cal[i][j], -1)
            if flaga[i] == -1:
                flagp[cal[i][j]] = cal[i][j]
                flaga[i] = cal[i][j]
            else:
                if keyp == -1:
                    flagp[cal[i][j]] = flaga[i]
                else:
                    # print keyp,flaga[i]
                    temp = flagp[cal[i][j]]
                    while flagp[temp] != temp:
                        temp = flagp[temp]
                    if temp > flaga[i]:
                        flagp[temp] = flaga[i]
                    else:
                        flagp[flaga[i]] = temp
    re = {}
    for i in range(len(flaga)):
        if flaga[i] != -1:
            while flagp[flaga[i]] != flaga[i]:
                flaga[i] = flagp[flaga[i]]
            re[flaga[i]] = re.get(flaga[i], 0) + 1
    return max(re.values())