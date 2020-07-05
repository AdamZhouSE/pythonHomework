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
        judgeNumber = False
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

def geLuc(num):
    if num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return geLuc(num-1)+geLuc(num-2)

testNumber = input[0][0]
count = 0
start = 1

while count < testNumber:
    print(geLuc(input[start][0]%1000000007))
    count += 1
    start += 1
