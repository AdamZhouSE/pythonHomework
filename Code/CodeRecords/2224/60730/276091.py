expression = list(map(int, str(input())))
length = len(expression)
ans = []
for i in range(length):
    if i != length - 1:
        ans = expression[i + 1:]
    if expression[i] < max(ans):
        m = expression.index(max(ans))
        expression[i], expression[m] = expression[m], expression[i]
        break
    else:
        continue
print(''.join(map(str, expression)))
