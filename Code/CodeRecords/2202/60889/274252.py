def brick(length):
    num1 = 0
    num2 = 1
    num3 = 1
    while length != 1:
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        length = length - 1
    print(num3)
    
numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    brick(length)