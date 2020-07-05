def happyNum(num):
    numAs = []
    while num!=1:
        numAs.append(num)
        newNum = 0
        while num!=0:
            remainder = num % 10
            newNum = remainder * remainder + newNum
            num = int(num/10)
        if numAs.count(newNum) != 0:
            return False
        num = newNum
    return True

numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    while True:
        num = num + 1
        if happyNum(num):
            print(num)
            break