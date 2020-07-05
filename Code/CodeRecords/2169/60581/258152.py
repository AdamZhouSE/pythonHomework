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
        if lst[i][j]=='+' or lst[i][j]=='-' or lst[i][j]=='*' or lst[i][j]=='/':
            judgeWord = True
            str += lst[i][j]
            theLine.append(str)

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
            theLine.append(str)
        j += 1
    input.append(theLine)

testNumber =int(input[0][0])

count = 0
start = 1

while count < testNumber:
    wordList = input[start].copy()
    stack = []

    for i in range(len(wordList)):
        if wordList[i]>='0' and wordList[i]<='9':
            stack.append(wordList[i])
        elif len(stack) >= 2:
            num1 = stack[len(stack) - 2]
            num2 = stack[len(stack) - 1]
            stack.remove(num1)
            stack.remove(num2)
            if wordList[i] == '+':
                stack.append(repr(int(num1)+int(num2)))
            elif wordList[i] == '-':
                stack.append(repr(int(num1)-int(num2)))
            elif wordList[i] == '*':
                stack.append(repr(int(num1)*int(num2)))
            elif wordList[i] == '/':
                stack.append(repr(int(num1)/int(num2)))
    print(stack[0])

    count += 1
    start += 1