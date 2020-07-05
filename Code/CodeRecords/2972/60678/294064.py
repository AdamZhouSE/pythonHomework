def findDifferIndex(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i
    return len(s)

n = int(input())
for i in range(n):
    s = input()
    t = input()
    if len(s) >= len(t) and s != t:
        print('No')
        continue
    else:
        # 长度方面没什么问题
        s = list(s)
        t = list(t)
        over = False
        while s != t:
            if len(s) == len(t):
                print('No')
                over = True
                break
            differIndex = findDifferIndex(s,t)
            differChar = t[differIndex]
            if differChar == s[differIndex - 1]:
                print('No')
                over = True
                break
            else:
                s.insert(differIndex, differChar)
        if not  over:
            print('Yes')