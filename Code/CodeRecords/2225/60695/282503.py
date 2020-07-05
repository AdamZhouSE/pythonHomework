n = int(input())
m = int(input())
res = 0
if m == 0:
    res = 1
elif n >= 3:
    res = 4 if m == 1 else 7 if m == 2 else 8
elif n == 2:
    res = 3 if m == 1 else 4
elif n == 1:
    res = 2
print(res)