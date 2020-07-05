num = int(input())
numAs = []
while num!=1:
    numAs.append(num)
    newNum = 0
    while num!=0:
        remainder = num % 10
        newNum = remainder * remainder + newNum
        num = int(num/10)
    if numAs.count(newNum) != 0:
        print(False)
        break
    num = newNum
else:
    print(True)
    