def romeNum(ch) -> str:
    if ch == 1:
        return 'I'
    elif ch == 5:
        return 'V'
    elif ch == 10:
        return 'X'
    elif ch == 50:
        return 'L'
    elif ch == 100:
        return 'C'
    elif ch == 500:
        return 'D'
    elif ch == 1000:
        return 'M'
    else:
        return ' '

trueNum = input()
para = len(trueNum) - 1
rome = ""

for num in trueNum:
    num = int(num)
    if num == 4 or num == 9:
        rome += romeNum(1 * pow(10, para))
        num += 1
        num *= pow(10, para)
        rome += romeNum(num)
    elif romeNum(num) == ' ':
        if num > 5:
            rome += romeNum(5 * pow(10, para))
            num -= 5

        while num > 0:
            rome += romeNum(1 * pow(10, para))
            num -= 1
    else:
        rome += romeNum(num * pow(10, para))

    para -= 1

print(rome)