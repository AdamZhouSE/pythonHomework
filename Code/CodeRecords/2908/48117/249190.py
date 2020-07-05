n = int(input())
wordList = []
wordSet = set()
for i in range(n):
    s = list(input())
    sList = list(s)
    sList.sort()
    s = str(sList)
    wordSet.add(s)

print(wordList)

