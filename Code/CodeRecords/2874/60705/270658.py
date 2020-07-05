# 不会连着两天健身: 不能是2 2 否则是2 0或者02
# 不能连着两天参加编程比赛：不能是11 否则是10或者01
# 3可以转化为1，也可以转化为2
days = int(input())
li = list(map(int, input().split(" ")))
xiuxiri = 0
today = li[0]
if today == 0:
    xiuxiri += 1
for i in range(1, days):
    if today == 0:
        if li[i] == 0:
            xiuxiri += 1
        today = li[i]
    elif today == 1:
        if li[i] == 1:
            today = 0
            xiuxiri += 1
        elif li[i] == 2:
            today = 2
        elif li[i] == 3:
            today = 2
        else:
            today = 0
            xiuxiri += 1
    elif today == 2:
        if li[i] == 0:
            xiuxiri += 1
            today = 0
        elif li[i] == 1:
            today = 1
        elif li[i] == 2:
            today = 0
            xiuxiri += 1
        else:
            today = 1
    else:
        if li[i] == 0:
            xiuxiri += 1
        today = li[i]
print(xiuxiri)
