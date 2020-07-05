s=str(input())
res = 0
sign = 1
num = 0
stack = []    
for c in s:
    if c.isdigit():
        num = 10 * num + int(c)
    elif c == '+' or c == '-':
        res = res + num * sign
        sign = 1 if c == '+' else -1
        num = 0
    elif c == '(':
        stack.append(res)
        stack.append(sign)
        sign = 1
        res = 0
    elif c == ')':
        res = res + sign * num
        old_sign = stack.pop()
        old_res = stack.pop()
        res = old_res + old_sign * res
        sign = 1
        num = 0
res = res + sign * num
print(res)

