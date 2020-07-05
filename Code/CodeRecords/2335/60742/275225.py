x = int(input())
y = int(input())
res = 0
while y>x:
    if y%2==0:
        y = y//2
        res += 1
    else:
        y += 1
        res += 1
res += x-y
print(res)