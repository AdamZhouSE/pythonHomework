n = int(input())
a = [int(i) for i in input().split()]
rise_end = 0
rise_time = 0
i = 1
while i < n:
    while i < n:
        if a[i - 1] <= a[i]:
            i += 1
            continue
        else:
            if rise_time == 0:
                rise_end = i
            break
    rise_time += 1
    i += 1
if rise_time > 2 or a[-1] > a[0]:
    res = -1
else:
    res = n - rise_time
print(res)