a = list(map(int, list(input())))
b = list(map(int, list(input())))
if len(a) < len(b):
    a = [0] * (len(b) - len(a)) + a
else:
    b = [0] * (len(a) - len(b)) + b

res = ""
carry = 0
for i in range(len(a) - 1, -1, -1):
    temp = a[i] + b[i] + carry
    if temp == 2:
        res = "0" + res
        carry = 1
    elif temp == 3:
        res = "1" + res
        carry = 1
    else:
        res = str(temp) + res
        carry = 0
if carry == 1:
    res ="1"+res
print(res)
