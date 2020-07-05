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
        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
            while judgeNumber:
                if j + 1 == len(lst[i]):
                    theLine.append(int(str))
                    break
                if lst[i][j+1] >= '0' and lst[i][j+1] <= '9':
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeNumber = False
                    theLine.append(int(str))
        j += 1
    input.append(theLine)

firstLine = input[0].copy()

nums = len(input[0])-2

numberList = firstLine[0:nums].copy()

k = firstLine[nums]
t = firstLine[nums+1]

judge = False

for i in range(nums-1):
    for j in range(i+1,nums):
        if j > i + k:
            break
        if (numberList[i]-numberList[j] >= 0 and numberList[i]-numberList[j]<=t) or (numberList[j]-numberList[i] >= 0 and numberList[j]-numberList[i]<=t):
            judge = True
            break
    if judge:
        break

if judge:
    print('true')
else:
    print('false')
