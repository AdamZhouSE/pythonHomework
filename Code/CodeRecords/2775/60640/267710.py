"""
三个连续整数之和
符合条件的有6，9，12，(3的倍数）
连续的三个数分别为 n/3-1 n/3 n/3+1
"""
t = int(input())
for i in range(t):
    n = int(input())
    if n >= 6 and n % 3 == 0:
        print(n//3-1, n//3, n//3+1)
    else:
        print(-1)
