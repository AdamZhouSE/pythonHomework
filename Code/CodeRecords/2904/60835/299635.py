i = input()
is_neg = False
n = i
if int(i) < 0:
    is_neg = True
    n = n[1:]
x = n[::-1]
res = int(x)
if is_neg:
    res = -res
print(res)