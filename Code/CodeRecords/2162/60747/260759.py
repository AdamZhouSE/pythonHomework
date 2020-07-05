s=input().split(",")
x=float(s[0])
n=int(s[1])
m = -n if n < 0 else n
p, q = 1, x
while m > 0:
    if (m&1) == 1:
        p *= q
    m //= 2
    q *= q
print(1/p if n < 0 else p)