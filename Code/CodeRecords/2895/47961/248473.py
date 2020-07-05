a=eval(input())
m=a[0]
n=a[1]
t = 0
while m != n:
    m >>= 1
    n >>= 1
    t += 1
print(n << t)

