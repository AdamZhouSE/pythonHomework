rawStr = input()[8:].split('], ')
s = rawStr[0].split(',')
k = int(rawStr[1][4])
t = int(rawStr[1][11])

for i in range(len(s)):
    s[i] = int(s[i])

hasPrint = False
for i in range(len(s)):
    for j in range(i, i + k + 1):
        if j == i:
            continue
        elif j >= len(s):
            break
        else:
            if abs(s[i] - s[j]) <= t:
                print('true')
                hasPrint = True
                break
    if hasPrint:
        break
if not hasPrint:
    print('false')