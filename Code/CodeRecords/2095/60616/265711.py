def addBinary( a, b):
    if len(a) < len(b):
        temp = a
        a = b
        b = temp
    a = a[::-1]
    b = b[::-1]
    extra = 0
    new_binary = ""
    for index, num in enumerate(a):
        if index > len(b) - 1:
            b_sum = 0
        else:
            b_sum = int(b[index])
        new_binary = new_binary + str((int(num) + b_sum + extra) % 2)
        if int(num) + b_sum + extra > 1:
            extra = 1
        else:
            extra = 0
    if extra == 1:
        new_binary = new_binary + "1"
    return new_binary[::-1]
a=input()
b=input()
print(addBinary(a,b))