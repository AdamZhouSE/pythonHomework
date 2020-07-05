a = int(input()) % 1337
b = list(map(int, input().split(',')))

rest = 1
for bi in b[::-1]:
    rest = (rest * (pow(a, bi) % 1337)) % 1337
    a = pow(a, 10) % 1337
print(rest)