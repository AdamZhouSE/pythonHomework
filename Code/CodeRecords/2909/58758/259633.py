def isvalid(bound, s):
    dic = {}
    for ch in s:
        dic[ch] = dic.get(ch, 0)+1
    if len(dic) <= bound:
        return True
    else:
        return False


s = input()
maxLetters = int(input())
minSize = int(input())
maxSize = int(input())
ans = 0
for i in range(0, len(s)-minSize):
    for j in range(i+minSize, i+maxSize+1):
        count = 0
        if isvalid(maxLetters, s[i: j]):
            ind = -1
            while True:
                try:
                    ind = s.index(s[i: j], ind+1)
                    count += 1
                except Exception:
                    break
            if count > ans:
                ans = count
print(ans)
