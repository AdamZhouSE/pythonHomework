n = int(input())
wordList = []
wordSet = set()
for i in range(n):
    s = input()
    wordList.append(s)
    s = list[s]
    sorted(s, key=lambda x: len(x))
    sStr = ''
    for i in s:
        sStr += i 
    wordSet.add(sStr)

print(wordList)