a = int(input())
num = 2
if a == 2:
    print(1)
elif a == 3:
    print(2)
elif a == 1:
    print(1)
else:
    for i in range(4, a + 1):
        x = 1
        for j in range(2, i - 1):
            if i % j == 0:
                x = 0
                break
        if x == 1:
            num = num + 1
    ans = 1
    for i in range(1, num + 1):
        ans = ans * i
    y = a - num
    for i in range(1, y + 1):
        ans = ans * i
    print(ans % (1000000000+7))