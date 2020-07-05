#!/usr/bin/python
# -*- coding: UTF-8 -*-
#四平方定理讲的就是任何一个正整数都可以表示成不超过四个整数的平方之和。
# 也就是说，这道题的答案只有 1，2 ，3，4 这四种可能。
# 同时，还有一个非常重要的推论满足四数平方和定理的数n（这里要满足由四个数构成，小于四个不行），必定满足 n = 4a * (8b + 7)。
# 根据这个重要的推论来解决此题，首先将输入的n迅速缩小。然后再判断，这个缩小后的数是否可以通过两个平方数的和或一个平方数组成，
# 不能的话我们返回3，能的话我们返回平方数的个数。
import math
n=int(input())
a=0
b=0
while(n%4==0):
    n//=4
if(n%8==7):
    print(4)
else:
    while(a*a<=n):
        b=int(math.pow((n-a*a),0.5))
        if(a*a+b*b==n):
            if(a!=0 and b!=0):
                print(2)
                break
            else:
                print(1)
                break
        a+=1
    if(a*a>n):
        print(3)