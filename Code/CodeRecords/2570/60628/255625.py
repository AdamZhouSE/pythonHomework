def maxEnvelopes(envelopes):
    res = 0
    envelopes.sort(key = lambda a: a[0])
    mem = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                mem[i] = max(mem[j] + 1, mem[i])
        res = max(res, mem[i])
    return res

num = int(input())
envelopes = [list(map(int, eval(input()))) for i in range(num)]
print(maxEnvelopes(envelopes))