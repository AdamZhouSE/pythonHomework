def fraction_to_circulator(dividend, divisor, precision=1000):
    if dividend//divisor==dividend/divisor:
        return dividend//divisor
    pos = 0
    modDict = {}
    frac = []
    is_circulator = False 
    div, mod = divmod(dividend, divisor)
    intPart = str(div) + '.'
    while pos < precision and mod != 0:
        modDict[mod] = pos
        mod *= 10
        div, mod = divmod(mod, divisor)
        frac.append(str(div))
        if mod in modDict.keys():
            is_circulator = True
            break
        pos += 1
    if is_circulator:
        frac.insert(modDict[mod], '(')
        frac.append(')')
    if len(frac)==0:
        return intPart
    return intPart + ''.join(frac)



dividend=int(input())
divisor=int(input())
print(fraction_to_circulator(dividend,divisor,1000))