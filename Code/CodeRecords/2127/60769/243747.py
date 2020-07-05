def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a % 1337
    else:
        return pow(a, b // 2) * pow(a, b - b // 2) % 1337


a = int(input())
b = list(map(int, input().split(",")))
res = 1
for i in b:
    res = pow(res, 10) * pow(a, i) % 1337
print(res)