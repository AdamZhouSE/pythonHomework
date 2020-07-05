def count(num):
    count = 0
    while num > 0:
        if num % 10 == 1:
            count += 1
        num = num // 10
    return count

n = int(input())
count1 = 0
for i in range(n+1):
    count1 += count(i)

print(count1)