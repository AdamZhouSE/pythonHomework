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

testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    inputNumber = input[start][0]
    place = 1
    while inputNumber > pow(2,place):
        inputNumber -= pow(2,place)
        place += 1
    inputNumber -= 1
    string = []
    while inputNumber > 0:
        if inputNumber % 2 == 0:
            string.insert(0,0)
        else:
            string.insert(0,1)
        inputNumber = int(inputNumber/2)
    while len(string)<place:
        string.insert(0,0)
    for i in range(len(string)):
        if string[i]==1:
            string[i] = '7'
        else:
            string[i] = '4'
    print("".join(string))

    count += 1
    start += 1