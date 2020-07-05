aa = input()
aaa = input().split(" ")
a = []
for i in range(len(aaa)):
    a.append(int(aaa[i]))
list.sort(a)
num = 0
four = 0
three = 0
two = 0
one = 0
for i in range(len(a)):
    if a[i] == 4:
        four = four + 1
    elif a[i] == 3:
        three = three + 1
    elif a[i] == 2:
        two = two + 1
    elif a[i] == 1:
        one = one + 1
num = num + four
if three > one:
    num = num + three
    one = 0
else:
    num = num + three
    one = one - three
if one != 0:
    num = num + one // 4
    one = one - 4 * (one // 4)
if two % 2 == 0:
    num = num + two / 2
    if one != 0:
        num = num + 1
else:
    num = num + two // 2
    if one > 2:
        num = num + 2
    else:
        num = num + 1
print(int(num))