s = input().strip()
Qidx = []
Aidx = []
for i in range(len(s)):
    if s[i] == 'Q':
        Qidx.append(i)
    elif s[i] == 'A':
        Aidx.append(i)
qNum = len(Qidx)
ans = 0
j = 0
for i in range(len(Aidx)):
    while Qidx[j] < Aidx[i]:
        j += 1
    ans += j*(qNum-j)
print(ans,end='')
