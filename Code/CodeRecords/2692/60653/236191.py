import re;

s = [int(n) for n in re.findall(r"\d+", input())]
D = int(input())
smax = 0
res = 0
for i in s:
    res += i
    if smax < i:
        smax = i
res = max(smax, res/D)
flag = True
while flag:
    sum = 0
    day = 1
    for i in s:
        if sum + i <= res:
            sum += i
        else:
            sum = i
            day += 1
    if day <= D:
        flag = False
    else:
        res += 1
print(int(res))