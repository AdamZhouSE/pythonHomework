a = [int(i)+1 for i in input().split(',')]
s = set(a)
res = 0
for i in s:
    res += i
print(res)