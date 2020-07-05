T = int(input())
while T > 0:
    M, X = input().split(" ")
    M = int(M)
    X = int(X)
    isE = False
    string = input().split(" ")
    nstr = [int(string[i]) for i in range(len(string))]
    nstr.sort()
    low = 0
    high = len(nstr) - 1
    while high > low:
        sum = nstr[low] + nstr[high]
        # print(nstr[low] + nstr[high])
        if sum == X:
            isE = True
            break
        elif sum > X:
            high -= 1
        else:
            low += 1
    if isE:
        print('Yes')
    else:
        print("No")
