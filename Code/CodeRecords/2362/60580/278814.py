n = int(input())
l = []
time = (n-1) // 4
remainder = (n-1) % 4
remainnum = 0

for i in range(time):
    l.append(int((n - i*4) * (n - i*4 - 1) / (n - i*4 - 2)))

if remainder == 0:
    remainnum = n - 4*time
elif remainder == 1:
    remainnum = (n - 4*time) * (n - 4*time - 1)
elif remainder == 2:
    remainnum = int((n - 4*time) * (n - 4*time - 1) / (n - time*4 - 2))
elif remainder == 3:
    remainnum = int((n - 4*time) * (n - 4*time - 1) / (n - time*4 - 2)) - (n - time*4 - 3)

if len(l) > 0:
    count = l[0]
    for i in range(1, len(l)):
        count -= l[i]
    for i in range(time):
        count += n - i*4 - 3
    count -= remainnum

else:
    if n == 4:
        count = 7
    elif n == 3:
        count = 6
    elif n == 2:
        count = 2
    else:
        count = 1

print(count)