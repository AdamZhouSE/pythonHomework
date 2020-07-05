times = int(input())
for looptimes in range(0, times):
    num = list(str(int(input())))
    while len(num) >= 2:
        sum = 0
        for i in num:
            sum += int(i)
        num = list(str(sum))
    print(str(num[0]))