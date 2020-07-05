num = eval(input())
n = int(input())
ans = 1
m = n if n >= 0 else -n
for i in range(m):
    ans *= num
print("{:.5f}".format(ans if n > 0 else 1 / ans))
