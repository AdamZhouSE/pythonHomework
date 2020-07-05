import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

subWordList = []

for i in range(0,len(lst[0])):
    if lst[0][i]>='a' and lst[0][i]<='z':
        subWordList.append(lst[0][i])
    else:
        break

wordList = []

for i in range(0,len(lst[1])):
    if lst[1][i]>='a' and lst[1][i]<='z':
        wordList.append(lst[1][i])
    else:
        break

next = 0
for i in range(len(subWordList)):
    judge = False
    for j in range(next,len(wordList)):
        if subWordList[i]==wordList[j]:
            judge = True
            next = j+1
            if next ==len(wordList):
                break
    if not judge:
        print(False)
        break

print(True)