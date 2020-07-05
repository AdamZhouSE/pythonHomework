x = float(input())
n = int(input())
result = 1
for i in range(n):
    result *= x
print('{0:.5f}'.format(result))
