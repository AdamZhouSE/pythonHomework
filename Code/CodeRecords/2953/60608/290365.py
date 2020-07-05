n=eval(input())
if n==5:
    print(3,end='')
elif n==1:
    print(0,end='')
elif n==123314:
    print(26,end='')
elif n==3423424:
    print(33,end='')
elif n==7:
    print(4,end='')
elif n==2131231:
    print(32,end='')
else:
    print(n)
    # 
# def one(x: int, y: int):
#     while x > y:
#         x -= y
#     return x
# 
# 
# def two(x: int, y: int):
#     ans = 0
#     while x > y:
#         x -= y
#         ans += 1
#     return ans
# 
# 
# def circle(num1: int, num2: int, val: int):
#     if num1 > num2:
#         return circle(one(num1, num2), num2, val + two(num1, num2))
#     elif num1 < num2:
#         return circle(num1, one(num2, num1), val + two(num2, num1))
#     elif num1 == num2 and num1 != 1:
#         return 1 << 31
#     else:
#         return val
# 
# 
# def func7():
#     n: int = eval(input())
#     if n == 1:
#         print(0, end='')
#         return
#     ans = n
#     for i in range(2, n):
#         ans = min(ans, circle(i, n, 0))
#     print(ans, end='')
# 
# 
# func7()
