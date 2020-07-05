questNum = int(input())

for quest in range(questNum):
    rawStr = input()

    s = ''
    for w in rawStr:
        if (ord(w) >= ord('a') and ord(w) <= ord('z')) or (ord(w) >= ord('A') and ord(w) <= ord('Z')):
            s += w.lower()

    l = 0
    r = len(s) - 1
    bad = False
    while l <= r:
        if s[l] != s[r]:
            print('NO')
            bad = True
            break
        l += 1
        r -= 1

    if not bad:
        print('YES')