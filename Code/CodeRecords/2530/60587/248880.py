S = input()
T = input()
nT = T
tmp = ''
for i in range(0, len(S)):
    num = T.count(S[i])
    tmp += S[i] * num
    nT = nT.replace(S[i], '')
    
res = tmp + nT
print(res)