def getAns(N):
    addition = 0
    ans = []
    tempRes = 1
    while tempRes <= N:
        ans.append(tempRes)
        tempRes = (tempRes << 1) + addition
        addition = 1 - addition
    return ans


T = eval(input())
for i in range(T):
    N = eval(input())
    print(*getAns(N))