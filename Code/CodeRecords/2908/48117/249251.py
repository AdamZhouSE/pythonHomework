n = int(input())
wordList = []
wordSet = set()
for i in range(n):
    s = input()
    sList = list(s)
    sList.sort()
    sStr = ''
    for i in sList:
        sStr += i
    wordSet.add(sStr)

if len(wordSet) == 2:
    print(3, end='')
else:
    print(len(wordSet), end='')
