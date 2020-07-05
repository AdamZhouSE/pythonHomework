N = int(input())
word = []
for i in range(N):
    s = ''+input()
    isExist = False
    for j in word:
        isSame = True
        if len(j) != len(s):
            continue
        else:
            for k in range(len(j)):
                if j.count(j[k]) != s.count(j[k]):
                    isSame = False
        if isSame:
            isExist = True
            break
    if not isExist:
        word.append(s)
print(len(word),end="")