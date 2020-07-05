num = int(input())
if num == 2:
    print(1)
elif num < 2:
    print(0)
else:
    count = 1
    for i in range(3, num + 1, 2):
        flag = True
        for j in range(3, int(num ** 0.5) + 1):
            if i % j == 0 and i != j:
                flag = False
                break
        if flag:
            count += 1
    print(count)