n = int(input())

count1 = 0
for num in range(1, n + 1):
    if '1' in str(num):
        count1 += 1

if '1' in str(n):
    count1 += 1

print(count1)