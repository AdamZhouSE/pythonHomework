m=eval(input())
a=m[0]
b=m[1]
t=0
while a!=b:
    a >>= 1
    b >>= 1
    t=t+1
print(b<<t)