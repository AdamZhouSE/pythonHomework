n = int(input())
group = list([int(n) for n in input().split()])
group.sort()
one = 0
two = 0
three = 0
four = 0
for i in group:
    if i == 1:
        one += 1
    if i == 2:
        two += 1
    if i == 3:
        three += 1
    if i == 4:
        four += 1
ans = four
flag = True
while flag:
    if two >= 2:
        two -= 2
        ans += 1
    elif one > 0 and three > 0:
        one -= 1
        three -= 1
        ans += 1
    else:
        flag = False

while three > 0:
    ans += 1
    three -= 1
if two > 0:
    if one >= 2:
        one -= 2
    if one == 1:
        one -= 1
    ans += 1
    two -= 1
while one > 0:
    if one >= 4:
        one -= 4
    else:
        one = 0
    ans += 1
print(ans)