def ishappy(n):
    flag = n
    if flag == 1:
        return True
    elif flag == 4:
        return False
    else:
        m = 0
        while n != 0:
            m += (n % 10) ** 2
            n //= 10
        n = m
        return ishappy(n)


count = int(input())
ans = []
for i in range(0, count):
    num = int(input()) + 1
    while not ishappy(num):
        num += 1
    ans.append(num)
for i in ans:
    print(i)
