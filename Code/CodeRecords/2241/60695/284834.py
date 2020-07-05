n = int(input())
count = 0

for i in range(1, n+1):
    sum = 0
    s = i
    flag = True
    while sum != n:
        sum += s
        s += 1
        if sum > n:
            flag = False
            break
    if flag:
        count += 1
print(count)