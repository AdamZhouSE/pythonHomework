def into_to_roman(n):
    r = ''
    ir = {'1000': 'M', '900': 'CM', '500': 'D', '400': 'CD', '100': 'C', '90': 'XC', '50': 'L',
          '40': 'XL', '10': 'X', '9': 'IX', '5': 'V', '4': 'IV', '1': 'I'}

    for k, v in ir.items():
        tmp = n // int(k)
        if tmp != 0:
            r += tmp * v
            n -= tmp * int(k)
    return r

a = int(input())
print(into_to_roman(a))















