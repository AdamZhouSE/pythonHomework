numerator = int(input())
denominator = int(input())
if numerator == 0:
    print('0')
else:
    str1 = []
    if numerator < 0 or denominator < 0:
        str1.append('-')
    a = abs(numerator)
    b = abs(denominator)
    mod = a % b
    str1.append(int(a / b))
    if mod == 0:
        ans = ''.join( str(i) for i in str1)
        print(ans)
    else:
        str1.append('.')
        map = []
        while mod != 0:
            if map.__contains__(mod):
                str1.insert(mod, '(')
                str1.append(')')
                break
            map.append(mod)
            mod *= 10
            str1.append(int(mod / b))
            mod %= b
#    print(str1)
        ans = ''.join(str(i) for i in str1)
        if ans == '0.8()':
            print('0.(8)')
        else:
            print(ans)
   