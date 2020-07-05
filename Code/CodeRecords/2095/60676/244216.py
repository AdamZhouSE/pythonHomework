def binary_addition(num1, num2):
    length = 1 + max(len(num1), len(num2))
    for i in range(length - len(num1)):
        num1 = '0' + num1
    for i in range(length - len(num2)):
        num2 = '0' + num2
    carry = 0
    res = ''
    for i in range(length):
        temp = carry + int(num1[length-i-1]) + int(num2[length-i-1])
        if temp == 0:
            res = '0' + res
            carry = 0
        elif temp == 1:
            res = '1' + res
            carry = 0
        elif temp == 2:
            res = '0' + res
            carry = 1
        else:
            res = '1' + res
            carry = 1
    if res[0] == 0:
        res = res[1:]
    return res


print(binary_addition(input(), input()))