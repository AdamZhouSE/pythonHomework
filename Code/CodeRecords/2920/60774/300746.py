s = input().split(' ')
n = int(s[0])
k = int(s[1])
numLst = list(map(int,input().split(' ')))
diff = [[i,numLst[i + 1] - numLst[i]] for i in range(0,n - 1)]
diff.sort(key = lambda x: -x[1])
breakpoint = [diff[i][0] for i in range(0,k - 1)]
breakpoint.sort()
value = 0
cur = 0
for p in breakpoint:
    temp = numLst[cur:p + 1]
    cur = p + 1
    value = value + temp[-1] - temp [0]
print(value)
        