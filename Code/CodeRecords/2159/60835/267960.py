num = int(input())
cnt = 0
result = ""
while num > 0:
    tem = num % 10
    if cnt == 0:
        if tem < 4:
            for n in range(tem):
                result = "I" + result
        elif tem == 4:
            result = "IV" + result
        elif tem == 9:
            result = "IX" + result
        else:
            for n in range(5,tem):
                result = "I" + result
            result = "V" + result
    elif cnt == 1:
        if tem < 4:
            for n in range(tem):
                result = "X" + result
        elif tem == 4:
            result = "XL" + result
        elif tem == 9:
            result = "XC" + result
        else:
            for n in range(5,tem):
                result = "X" + result
            result = "L" + result
    elif cnt == 2:
        if tem < 4:
            for n in range(tem):
                result = "C" + result
        elif tem == 4:
            result = "CD" + result
        elif tem == 9:
            result = "CM" + result
        else:
            for n in range(5,tem):
                result = "C" + result
            result = "D" + result
    else:
        result = "M" + result
    cnt = cnt + 1
    num = num // 10
print(result)     