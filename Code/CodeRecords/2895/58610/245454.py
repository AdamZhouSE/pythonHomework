a = eval(input())
res = -1
for num in range(a[0], a[1] + 1):
    res = res & num
print(res)