T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    string = input().split(" ")
    nstr = [int(string[i]) for i in range(len(string))]
    # print(nstr)
    res = -1
    for i in range(1, length - 1):
        isAllSmall = True
        isAllLarge = True
        for j in range(0, i):
            if nstr[j] > nstr[i]:
                isAllSmall = False
                isAllLarge = False
                break
        if isAllSmall:
            for k in range(i, length):
                if nstr[k] < nstr[i]:
                    isAllLarge = False
                    break
        if isAllLarge:
            res = nstr[i]
            break
    print(res)
