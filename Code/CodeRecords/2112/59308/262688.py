a = [int(x) for x in input().split(',')]
k = len(a)+1
s = k * (k - 1) / 2
for i in a:
    s -= i
print(int(s))
