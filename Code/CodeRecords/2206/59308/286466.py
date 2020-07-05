#coding=utf8

T = int(input())
point = 1
s = 0
res = []
j = 1
while point < 15:
    temp = point
    i = 1
    while temp > 0:
        i = i * j
        j += 1
        temp -= 1
    s += i
    res.append(s)
    point += 1
for _ in range(T):
    a = int(input())
    print(res[a-1])