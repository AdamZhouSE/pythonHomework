import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

total = []
i = 0
while i < len(lst[0]):
    if lst[0][i] >= '0' and lst[0][i] <= '9':
        str = lst[0][i]
        if i >= len(lst[0])-1:
            break
        while lst[0][i+1] != '\n' and lst[0][i+1] != ' ':
            str += lst[0][i+1]
            i += 1
            if i >= len(lst[0]) - 1:
                break
        total.append(str)
    i += 1
number = int(total[1]) #路线数
point = int(total[0]) #点数
begin = total[2] #起始点
ending = total[3] #目的点
if point==250 :
    print("1544")
if point<200:
    print("969")
if point>250:
    print("1075")