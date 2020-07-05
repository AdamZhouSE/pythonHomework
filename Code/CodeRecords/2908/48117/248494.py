n = int(input())
wordList = []
wordSet = set
for i in range(n):
    s = input()
    wordSet.add(s)

print(len(wordSet))