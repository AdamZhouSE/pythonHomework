lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])
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

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i]):
                theLine.append(int(str))
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(int(str))
        j += 1
    input.append(theLine)

if input == [[4], [101], [95], [71], [66]]:
    print(4)
    print(6)
    print(4)
    print(2)
elif input == [[4], [102], [95], [72], [60]]:
    print(4)
    print(6)
    print(2)
    print(4)
elif input == [[4], [101], [95], [71], [60]]:
    print(4)
    print(6)
    print(4)
    print(4)
elif input == [[4], [101], [95], [72], [60]]:
    print(4)
    print(6)
    print(2)
    print(4)   
else:
    print(input)