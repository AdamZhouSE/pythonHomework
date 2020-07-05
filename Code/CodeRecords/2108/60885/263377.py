n = int(input())
count = 0
for i in range(1, n+1):
    temp = str(i)
    for c in temp:
        if c == '1':
            count += 1

print(count)