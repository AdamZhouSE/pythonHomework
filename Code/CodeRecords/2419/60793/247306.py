n = input()
ls = [int(x) for x in n]
add = 0
mul = 1
for i in ls:
    mul *= i
for i in ls:
    add += i
print(mul)
print(add)