import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

wordList = []
i = 0
while i < len(lst[0]):
    judge = False
    word = ''
    if lst[0][i]>='0' and lst[0][i]<='9':
        word += lst[0][i]
        judge = True
        i += 1
    while judge:
        if i == len(lst[0]):
            wordList.append(int(word))
            judge = False
            break
        else:
            if lst[0][i]>='0' and lst[0][i]<='9':
                word += lst[0][i]
            else:
                wordList.append(int(word))
                judge = False
            i += 1

if wordList[0]>=wordList[3] and wordList[1]<=wordList[2]:
    print(True)
else:
    print(False)