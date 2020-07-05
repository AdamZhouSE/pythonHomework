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
        judgeWord = False
        judgeNumber = False
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
            theLine.append(str)
        j += 1
    input.append(theLine)

str1 = input[0].copy()
str2 = input[0].copy()

i = 0
j = 0
while i < len(str2) and j < len(str1):
    if str2[i:].count(str1[j]) > 0:
        str2[i:].remove(str1[j])
        str2.insert(i,str1[j])
        i += 1
    else:
        j += 1

print("".join(str2),end="")
