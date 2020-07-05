def noZero(n:int):
    return '0' not in str(n)


n = eval(input())
a = 0
b = 0
for i in range(n):
    a = i
    b = n - i
    if noZero(a) and noZero(b):
        break
re = [a,b]
print(re)