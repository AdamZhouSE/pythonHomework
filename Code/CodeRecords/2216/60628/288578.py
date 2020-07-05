def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a, b = b, r
    return a if a > 0 else -a

def fractionAddition(num1, num2):
    sum1 = int(num1[0]) * int(num2[1]) + int(num2[0]) * int(num1[1])
    sum2 = int(num1[1]) * int(num2[1])
    gcd = GCD(sum1, sum2)
    return [int(sum1 / gcd), int(sum2 / gcd)]

def fractionSubtraction(num1, num2):
    sum1 = int(num1[0]) * int(num2[1]) - int(num2[0]) * int(num1[1])
    sum2 = int(num1[1]) * int(num2[1])
    gcd = GCD(sum1, sum2)
    return [int(sum1 / gcd), int(sum2 / gcd)]

def expressionOperation(exp):
    num1 = [0, 1]
    if exp[0] != '-':
        exp = '+' + exp
    for i in range(len(exp)):
        if exp[i] == '+':
            num2 = [exp[i+1], exp[i+3]]
            num1 = fractionAddition(num1, num2)
        if exp[i] == '-':
            num2 = [exp[i + 1], exp[i + 3]]
            num1 = fractionSubtraction(num1, num2)

    return num1

exp = input()
res = expressionOperation(exp)
print(str(res[0])+'/'+str(res[1]))