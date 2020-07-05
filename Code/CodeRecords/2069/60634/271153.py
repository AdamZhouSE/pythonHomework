def leftMove(num):
    return num + '0'
def add(a1,a2):
    if len(a1) < len(a2):
        n1 = a2
        n2 = a1
    else:
        n1 = a1
        n2 = a2
    for x in range(abs(len(a1)-len(a2))):
        n2 = '0' + n2
    result = ""
    carry = 0
    i = len(n1) - 1
    while i >= 0:
        temp = int(n1[i]) + int(n2[i]) + carry
        carry = int(temp/10)
        result = str(temp%10) + result
        i -= 1
    if carry != 0:
        result = str(carry) + result
    return result
def mul(m1,m2):
    result = "0"
    i = 0
    while i < len(m1):
        for x in range(int(m1[i])):
            result = add(result,m2)
        if i < len(m1) - 1:
            result = leftMove(result)
        i += 1
    return result

#main-----
print(mul(input(),input()))

