def changeToRome(text):
    num = int(text)

    # 数组内数据位置不要改，不然就不能从高位开始对比
    checkNum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    i = 0

    # 对比完，减去已对比数组，对比数组下个值
    while (num != 0):
        if (num >= checkNum[i]):
            num -= checkNum[i]
            roman += str[i]
        else:
            i += 1

    return roman

text = input()
print(changeToRome(text))
