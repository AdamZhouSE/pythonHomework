import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

number = int(lst[0])
wordList = []
i = 0
while i < len(lst[1]):
    judge = False
    word = ''
    if lst[1][i]>='0' and lst[1][i]<='9':
        word += lst[1][i]
        judge = True
        i += 1
    while judge:
        if i == len(lst[1]):
            wordList.append(int(word))
            judge = False
            break
        else:
            if lst[1][i]>='0' and lst[1][i]<='9':
                word += lst[1][i]
            else:
                wordList.append(int(word))
                judge = False
            i += 1

def judgeNumber(number,wordList):
    for i in range(0,len(wordList)):
        while number%wordList[i]==0:
            number = number/wordList[i]
    if number==1:
        return True
    else:
        return False


count = 0
start = 1
while count < number:
    if judgeNumber(start,wordList):
        count += 1
    start += 1

print(start-1)