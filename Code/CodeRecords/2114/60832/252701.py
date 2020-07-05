# 此题采用数学原理 四平方定理：任何一个正整数都可以表示成不超过四个整数的平方之和。
# 及推论：满足四数平方和定理的数n（这里要满足由四个数构成，小于四个不行），必定满足 n = 4^a * (8b + 7)

import math

x = int(input())

while x % 4 == 0:
    x = x / 4

if x % 8 == 7:
    print(4)
    exit()

while x%9==0:
    x=x/9
a=0
judge=x/2
while a*a<=judge:
    b=int(math.pow(x-a*a,0.5))
    if a*a+b*b==x:
        if a==0:
            print(1)
        else:
            print(2)
        exit()
    a+=1
print(3)
