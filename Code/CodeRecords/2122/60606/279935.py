def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
x = int(input())
y = int(input())
#如果是z是可以取到的，那么必定是gcd(x,y)的整数倍
z = int(input())
if z%gcd(x,y)==0:
    print("True")
else:
    print("False")
