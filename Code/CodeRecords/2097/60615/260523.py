dividend = int(input())
divisor = int(input())


def converter(dividend,divisor):

    integar,decimal=map(str,str(dividend/divisor).split('.'))

    dec=''
    if len(decimal)==16:
        for item in decimal[:15]:
            if item not in dec:
                dec=dec+item
        dec='.('+dec+')'
    elif decimal=='0':
        dec=''
    else:
        dec='.'+decimal
    return integar+dec

print(converter(dividend,divisor))