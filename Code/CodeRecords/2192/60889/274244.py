numOfInput = int(input())
for i in range(numOfInput):
    num1 = int(input())
    num2 = num1
    while num1 > 0:
        print(num1,end = " ")
        num1 = num1 - 5
    while num1 != num2:
        print(num1,end = " ")
        num1 = num1 + 5
    print(num1,end=" \n")
    