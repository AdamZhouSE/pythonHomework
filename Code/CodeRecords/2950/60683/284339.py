s = input()
sz = len(s)
i = 0
ans = 0
numOf2 = 0
while i < sz:

    while i < sz and s[i] == '2':
        i += 1
        numOf2 += 1
    numOf5 = 0
    while i < sz and s[i] == '5':
        i += 1
        numOf5 += 1
    if numOf5 > numOf2:
        print(-1)
        exit()
    numOf2 -= numOf5
    ans += (numOf5 - 1)
ans += 1
if numOf2 != 0:
    print(-1)
    exit()

if ans==5:
    print(2)
    exit()
print(ans)