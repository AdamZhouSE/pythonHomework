questNum = int(input())

count = 0

for i in range(questNum):
    s = input()
    wordList = []

    for w in s:
        if w in wordList:
            continue
        else:
            count += s.count(w) - 1
            wordList.append(w)

    print(count)