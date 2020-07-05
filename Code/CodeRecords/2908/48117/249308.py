n = int(input())
wordSet = set()
for i in range(n):
    s = input()
    sList = list(s)
    sList.sort()
    sStr = ''
    for j in sList:
        sStr += j
    wordSet.add(sStr)

print(len(wordSet), end='')