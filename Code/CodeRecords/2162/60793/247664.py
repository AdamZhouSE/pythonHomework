ls = list(map(float, input().split(",")))
a = ls[0]
b = int(ls[1])
result = 1
while b != 0:
    result *= a
    b -= 1
print(result)