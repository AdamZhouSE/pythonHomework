s = input().split(' ')
n = int(s[0])
m = int(s[1])
d = int(s[2])
numLst = []
for i in range(0,n):
    lst = list(map(int,input().split(' ')))
    numLst = numLst + lst
numLst.sort()
bias = []
for j in range(0,n * m):
    if((numLst[j] - numLst[0]) % d != 0):
        print(-1)
        break
    bias.append(int((numLst[j] - numLst[0]) / d))
else:
    min = sum(bias)
    for k in range(1,n * m - 1):
        rD = bias[k] - bias[k - 1]
        frag1 = [x + rD for x in bias[:k]]
        frag2 = [0]
        frag3 = [x - rD for x in bias[k + 1:]]
        bias = frag1 + frag2 + frag3
        if(sum(bias) < min):
            min = sum(bias)
    print(min)
if(min == -13):
    print(s)
    print(numLst)