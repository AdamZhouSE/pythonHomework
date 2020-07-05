large_unit = {'Billion': 1000000000,'Million': 1000000,'Thousand': 1000}
second_unit = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
ten_unit = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
digit = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

def translate(num):
    if num == 0:
        return 'Zero'
    result = []
    for unit, base in large_unit.items():
        if num >= base:
            result.append(translate(int(num/base)))
            result.append(unit)
            num %= base
    if num >= 100:
        result.append(digit[int(num/100)-1])
        result.append('Hundred')
        num %= 100
    if num >= 20:
        result.append(second_unit[int(num/10)-2])
        num %= 10
    elif num >= 10:
        result.append(ten_unit[num-10])
        num = 0
    if num > 0:
        result.append(digit[num-1])
    return ' '.join(result)

n = int(input())
result = translate(n)
print(result)