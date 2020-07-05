n = int(input())
wordList = []
wordSet = set()
for i in range(n):
    s = list(input())
    sStr = ''
    for j in s:
        sStr += j
    wordList.append(sStr)
    s = list[s]
    sorted(s, key=lambda x: len(x))
    sStr = ''
    for j in s:
        sStr += j
    wordSet.add(sStr)

print(wordList)

print(wordList)