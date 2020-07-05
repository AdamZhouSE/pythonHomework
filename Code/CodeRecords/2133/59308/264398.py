a = [int(x) for x in input().split(',')]
m = min(a)
s = 0
for i in a:
    s += i - m
print(s)


