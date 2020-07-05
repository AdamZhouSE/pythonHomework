questNum = int(input())

for quest in range(questNum):
    s = input()

    ans = []
    maxLen = 0
    for i in range(len(s) - 1):
        temp = s[i]
        for j in range(i + 1, len(s)):
            if ord(s[j]) <= ord(s[i]):
                if len(temp) >= maxLen:
                    ans.append(temp)
                    maxLen = len(temp)
                break
            else:
                temp += s[j]

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