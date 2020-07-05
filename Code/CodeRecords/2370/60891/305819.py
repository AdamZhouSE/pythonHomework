n = int(input())
ans = []
while n != 0:
    if (n - 1) % 2 == 0:
        ans.append(1)
        n -= 1
    else:
        ans.append(0)
    n //= (-2)
ans = ans[::-1]
for i in ans:
    print(i, end='')
