n = int(input())
base = list(range(1, n+1))
count = 1
for i in range(len(base)):
    tmp = base[i]
    for j in range(i+1, len(base)):
        tmp += base[j]
        if tmp == n:
            count += 1
            break
        elif tmp > n:
            break
print(count)
