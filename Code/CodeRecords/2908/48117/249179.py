n = int(input())
wordList = []
wordSet = set()
for i in range(n):
    s = list(input())
    wordSet.add(s)

print(len(wordSet))

