x = list(map(int, input()[:-1].split('+')))
y = list(map(int, input()[:-1].split('+')))
res = ''
res += str(x[0] * y[0] - x[1] * y[1]) + '+'
res += str(x[1] * y[0] + x[0] * y[1]) + 'i'
print(res)
