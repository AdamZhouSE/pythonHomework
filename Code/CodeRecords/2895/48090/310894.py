num=list(input())
a=int(num[1])
b=int(num[3])


t = 0
while a != b:
    a >>= 1
    b >>= 1
    t += 1
print(b << t)