def fix(s,l):
    for x in range(l):
        s = '0' + s
    return s


def add(a,b):
    i = len(a)-1
    if len(a) > len(b):
        b = fix(b,len(a)-len(b))
    elif len(b) > len(a):
        i = len(b)-1
        a = fix(a,len(b)-len(a))
    result = ""
    carry = 0
    while i >= 0:
        temp = carry + int(a[i]) + int(b[i])
        if temp == 0:
            carry = 0
            result = '0' + result
        elif temp == 1:
            carry = 0
            result = '1' + result
        elif temp == 2:
            carry = 1
            result = '0' + result
        elif temp == 3:
            carry = 1
            result = '1' + result
        i -= 1
    if carry == 1:
        result = '1' + result
    return result


#main-----
a = input()
b = input()
print(add(a,b))
