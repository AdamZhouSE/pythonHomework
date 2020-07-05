list = eval(input())
m = list[0]
n = list[1]

t = 0
while m != n:
    m >>= 1
    n >>= 1
    t += 1

print(n << t)
 