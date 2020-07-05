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

def calculate(num):
    lst = ""
    while num > 0:
        if num % 2 == 0:
            lst = "0" + lst
        else:
            lst = "1" + lst
        num = int(num/2)
    return lst

testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    num = input[start][0]
    for i in range(1,num):
        print(calculate(i),end=" ")
    print(calculate(num),end=" ")
    print()

    count += 1
    start += 1