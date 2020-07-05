def f(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return f(n-1) + f(n-2)


t = int(input())
num = []
for i in range(0, t):
    num.append(int(input()))
for i in range(0, t):
    print(f(num[i]))