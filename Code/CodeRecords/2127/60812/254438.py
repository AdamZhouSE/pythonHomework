a = int(input())
l = 1
b = int(''.join(i for i in input().split(',')))
while b != 0:
    l *= a
    if l > 1337:
        l %= 1337
    b -= 1
print(l)