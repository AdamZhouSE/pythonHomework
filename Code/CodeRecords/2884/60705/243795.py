line1 = list(map(int, input().split(" ")))
n = line1[0]
x = line1[1]
count = 0
line2 = list(map(int, input().split(" ")))
for i in range(0, n-1):
    for j in range(i+1, n):
        if abs(line2[i] - line2[j]) <= x:
            count += 2

print(count)
