numOfInput = int(input())
for i in range(numOfInput):
    inputNum = int(input())
    outputNum = 1
    while(inputNum > outputNum):
        outputNum = outputNum * 2
    print(outputNum)