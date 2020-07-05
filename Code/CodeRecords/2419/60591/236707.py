n = list(map(int,list(input())))
a = 1
b = 0
for x in n:
    a *= x
    b += x
print(a-b)