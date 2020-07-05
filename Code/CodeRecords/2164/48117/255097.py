questNum = int(input())

count = 0
wordList = []
for i in range(questNum):
    s = input()

    for w in s:
        if w in wordList:
            continue
        else:
            count += s.count(w) - 1
            wordList.append(w)

    print(count)