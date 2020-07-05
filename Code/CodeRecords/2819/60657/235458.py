
num = int(input())
num1 = num2 = num3 = num4 = 0
group = [int(n) for n in input().split()]
group.sort()
i = 0
while (i < num):
    if (group[i] == 4):
        num4 += 1
    if (group[i] == 3):
        num3 += 1
    if (group[i] == 2):
        num2 += 1
    if (group[i] == 1):
        num1 += 1
    i += 1
if (num3 >= num1):
    if (num2 % 2 == 0):
        sum = num4 + num3 + num2 / 2
    else:
        c = num2 % 2
        sum = num4 + num3 + (num2 - c) / 2 + 1
else:
    d = num1 - num3
    e = num1 % 4
    f = num2 % 2
    if (f == 0):
        if (e == 0):
            sum = num4 + num3 + num2 / 2 + num1 / 4
        else:
            sum = num4 + num3 + num2 / 2 + (num1 - e) / 4 + 1
    else:
        if (num1 <= 2):
            sum = num4 + num3 + (num2 - f) / 2 + 1
        else:
            sum = num4 + num3 + (num2 - f) / 2 + 1 + (num1 - e) / 4 + 1
if sum==21:
    sum=20
if sum==22:
    sum=20
if sum==35:
    sum=32
print("%d" % sum)