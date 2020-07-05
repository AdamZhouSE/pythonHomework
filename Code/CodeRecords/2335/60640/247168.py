"""
坏了的计算器
逆向思维
Y可以加1或者除以2，
如果X<Y,那么让Y尽可能的除以2，以接近X
如果X>Y,那么Y只能不断加1
"""
x = int(input())
y = int(input())
if x >= y:
    print(x-y)
else:
    count = 0
    while y > x:
        y //= 2
        count += 1
    count += x - y
    print(count)
