questNum = int(input())

for quest in range(questNum):
    s = input()

    ans = []
    maxLen = 1
    temp = ''
    for i in range(len(s) - 1):
        if len(temp) >= maxLen and len(temp) != 1:
            ans.append(temp)
        temp = s[i]
        gap = 0
        for j in range(i + 1, len(s)):
            if ord(s[j]) <= ord(s[j - 1]):
                if len(temp) >= maxLen and len(temp) != 1:
                    ans.append(temp)
                    maxLen = len(temp)
                break
            else:
                if gap == 0:
                    gap = ord(s[j]) - ord(s[j - 1])
                    temp += s[j]
                else:
                    if ord(s[j]) - ord(s[j - 1]) == gap:
                        temp += s[j]
                    else:
                        if len(temp) >= maxLen and len(temp) != 1:
                            ans.append(temp)
                            maxLen = len(temp)
                        break

    maxOrd = 0
    ansStr = ''
    for t in ans:
        tOrd = 0
        for w in t:
            tOrd += ord(w)
        if tOrd > maxOrd:
            ansStr = t
            maxOrd = tOrd

    print(ansStr[::-1])