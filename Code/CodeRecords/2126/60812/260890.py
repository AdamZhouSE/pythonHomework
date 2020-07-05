nums = sorted(int(i) for i in input().split(','))
t = []
for i in nums:
    for j in t:
        if i % j[0] == 0:
            j.insert(0, i)
            break
    else:
        t.append([i])
num = 0
temp = []
for i in t:
    if len(i) > num:
        num = len(i)
        temp = i
print(sorted(temp))