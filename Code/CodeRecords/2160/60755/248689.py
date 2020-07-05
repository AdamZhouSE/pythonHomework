a = int(input())
b = int(input())
flag = 0
if a*b<0:
    flag  = 1
a = abs(a)
b = abs(b)
res = 0
while a >= b:
    a = a - b
    res = res + 1
if flag :
    res = - res
print(res)