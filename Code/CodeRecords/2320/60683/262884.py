S = input()
K = eval(input())
minS = S
if K == 1:
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < minS:
            minS = S
else:
    ss = list(S)
    ss.sort()
    minS = ''.join(ss)
print(minS)