a = int(input())
if a < 0:
    print("-", end="")
    a = -a
res = 0
len = len(str(a))
for i in range(len, 0, -1):
    res *= 10
    res += int(str(a)[-1])
    a //= 10
print(res)
