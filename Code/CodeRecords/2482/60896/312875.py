def fraction_to_circulator(dividend, divisor, precision=1000): 
    '''
        把分数转换为循环小数。
        理论依据：任何分数都可以转换为有限小数或者无限循环小数。
        Args:
            dividend： 被除数
            divisor：  除数
            precision：精度。即计算循环小数时，最多计算到的小数点后多少位
        Returns:
            循环小数(字符串)。格式为：1.2(34)。括号中的是循环体。
    '''
    if(dividend%divisor==0):
        return(int(dividend/divisor))
    pos = 0
    modDict = {}
    frac = []
    is_circulator = False       #是否存在循环
    
    div, mod= divmod(dividend, divisor) 
    intPart = str(div) + '.' 
    
    #模拟手算的过程，发现有相同的余数就说明发现循环
    while pos < precision and mod != 0 : 
        modDict[mod] = pos 
        mod *= 10 
        div, mod = divmod (mod, divisor) 
        frac.append(str(div)) 
        if mod in modDict.keys():
            is_circulator = True
            break 
        pos += 1 
        
    if is_circulator:                       # 发现循环 
        frac.insert(modDict[mod],'(') 
        frac.append(')') 
    return intPart + ''.join(frac)

n=eval(input())
for i in range(n):
    a=eval(input())
    b=eval(input())
    print(fraction_to_circulator(a,b))