import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
            theLine.append(str)
        j += 1
    input.append(theLine)

str1 = input[0].copy()
str2 = input[1].copy()
length1 = len(str1)
length2 = len(str2)
count = 0
for i in range(0,length1-length2+1):
    judge = True
    for j in range(0,len(length2)):
        if length1[i+j] != length2[j]:
            judge = False
            break
    if judge:
        count += 1
print(count)