inp = input()
stack = []
sign = 1
num = 0
res = 0

for c in inp:
    if c.isdigit():
        num = num * 10 + int(c)
    elif c == "+":
        res += sign * num
        num = 0
        sign = 1
    elif c == "-":
        res += sign * num
        num = 0
        sign = -1
    elif c == "(":
        stack.append(res)
        stack.append(sign)
        sign = 1
        res = 0
    elif c == ")":
        res += sign * num
        num = 0
        res = stack.pop() * res + stack.pop()
res += sign * num
print(res)
