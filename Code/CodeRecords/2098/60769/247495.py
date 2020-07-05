num = int(input())
res = ""
while num > 0:
    temp = num % 26
    num = num // 26
    if temp == 0:
        temp = 26
        num -=1
    res = chr(64 + temp) + res
print(res)
