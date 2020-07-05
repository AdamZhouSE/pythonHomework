str = input()
str = str.strip().rstrip()
if not str:
    print('0')
res = 0
sign = -1 if str[0] == '-' else 1
i = 1 if str[0] in ['+', '-'] else 0
while i < len(str) and str[i] >= '0' and str[i] <= '9':
    res = res * 10 + (ord(str[i]) - ord('0'))
    i += 1
# 注意要乘符号，注意是放在res更新之后
if res * sign > 2147483647:
    print( 2147483647)
elif res * sign < -2147483648:
    print( -2147483648)
else:
    print(res * sign)

