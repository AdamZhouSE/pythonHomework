a = input()
b = input()
ans1 = 0
for i in range(len(a) - 1, -1, -1):
    ans1 += int(a[i]) * pow(2, len(a) - i - 1)
ans2 = 0
for i in range(len(b) - 1, -1, -1):
    ans2 += int(b[i]) * pow(3, len(b) - i - 1)
flag = True
if ans1 > ans2:
    temp = ans1 - ans2
else:
    temp = ans2 - ans1
    flag = False
while True:
    i = 1
    temp -= pow(2, i)
    if temp % 3 is 0:
        if flag:
            print(ans2 + temp)
        else:
            print(ans2 - temp)
        break


