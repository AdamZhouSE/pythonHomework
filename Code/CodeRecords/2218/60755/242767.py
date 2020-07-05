num = input().split(",")
all = 1
for i in num:
    all = all * int(i)
if len(num) == 3:
    print(all)
else:
    while len(num) != 3:
        max = 0
        for i in num:
            if all/int(i) > max:
                max = int(all / int(i))
        re = str(int(all/max))
        num.remove(re)
        all = max
    print(max)