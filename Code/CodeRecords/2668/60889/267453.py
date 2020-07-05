numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    newNum = 1
    while num>newNum:
        newNum = newNum * 2 + 1
    print(str(newNum-num)+" "+str(newNum))