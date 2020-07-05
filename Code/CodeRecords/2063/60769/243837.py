a = int(input())

b =a
if a < 0:
    a = -a
res = 0
len = len(str(a))
for i in range(len, 0, -1):
    res *= 10
    res += int(str(a)[-1])
    a //= 10
print(res==b)