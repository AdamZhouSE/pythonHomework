n = int(input())
wordList = []
wordSet = set()
for i in range(n):
    s = input()
    sList = list(s)
    sList.sort()
    sStr = ''
    for i in sList[1:-1]:
        sStr += i
    wordSet.add(sStr)

print(len(wordSet), end='')

