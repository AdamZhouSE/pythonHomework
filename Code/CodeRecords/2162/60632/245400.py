x = float(input())
n = int(input())
result = 1
for i in range(abs(n)):
    result *= x
if n < 0:
    print('{0:.5f}'.format(1 / result))
else:
    print('{0:.5f}'.format(result))
