numerator = int(input())
denominator = int(input())
res = ''
remainder = 0
index = 0
dict_num = {}
if numerator == denominator:
    res = '1'
elif numerator > denominator:
    remainder = numerator % denominator
    numerator = int(numerator / denominator)
    if remainder != 0:
        res = str(numerator) + '.'
    else:
        res = str(numerator)
elif numerator < denominator:
    numerator = numerator * 10
    remainder = numerator % denominator
    numerator = int(numerator / denominator)
    if remainder != 0:
        res = '0.'
    else:
        res = '0.' + str(numerator)
while remainder != 0:
    index = index + 1
    if remainder not in dict_num.keys():
        dict_num[remainder] = index
        remainder = remainder * 10
        quotient = int(remainder / denominator)
        remainder = remainder % denominator
        res = res + str(quotient)
    else:
        res_list = list(res)
        index_insert = dict_num[remainder] + res_list.index('.')
        res_list.insert(index_insert, '(')
        res_list.append(')')
        res = ''.join(res_list)
        break
print(res)