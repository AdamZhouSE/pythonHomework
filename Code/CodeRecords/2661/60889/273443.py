def xor(num1,num2):
    now = 1
    answer = 0
    while (num1!=0)or(num2!=0):
        if (num1%2)+(num2%2) == 1:
            answer = answer + now
        now = now * 2
        num1 = int(num1/2)
        num2 = int(num2/2)
    return answer
        

numOfInput = int(input())
for i in range(numOfInput):
    num = int(input())
    numOf0 = 0
    numOf1 = 0
    while num!=0:
        if num%2 == 0:
            numOf0 = numOf0 + 1
        else:
            numOf1 = numOf1 + 1
        num = int(num/2)
    print(xor(numOf1,numOf0))
    