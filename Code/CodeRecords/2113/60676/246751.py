# 将非负整数转换为其对应的英文表示。可以保证给定输入小于 2^31 - 1 。


DICTIONARY1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
              'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
DICTIONARY2 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
DICTIONARY3 = ['', 'Thousand', 'Million', 'Billion']


def three_digits_transformer(num):
    res = ''
    if num >= 100:
        res += DICTIONARY1[num//100] + ' Hundred '
    if num % 100 > 20:
        res += DICTIONARY2[(num % 100)//10] + ' ' + DICTIONARY1[(num % 10)]
    else:
        res += DICTIONARY1[num % 100]
    return ' ' + res


def translator(num):
    level = 0
    copy = num
    res = ''
    while copy > 0:
        res = ' ' + DICTIONARY3[level] + res
        res = three_digits_transformer(copy % 1000) + res
        copy //= 1000
        level += 1
    return res[1:-1]


print(translator(int(input())))