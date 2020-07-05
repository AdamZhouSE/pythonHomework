num = int(input())
count = 0
while num != 1:
    if num % 2 == 0:
        num = num // 2
        count += 1
    else:
        num = num -1
        count += 1
print(count)
