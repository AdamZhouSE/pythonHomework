s = input().strip()
sign = 1
num = 0
if not s:
    num = 0
else:
    if s[0] == "+":
        s = s[1:]
    elif s[0] == "-":
        sign = -1
        s = s[1:]
    for c in s:
        if "0" <= c <= "9":
            num = num*10 + ord(c) - ord('0')
        else:
            break
    num *= sign
    if num > 2147483647:
        num = 2147483647
    if num < -2147483648:
        num = -2147483648
print(num)