n = int(input())
a = [int(i) for i in input().split()]
total_n = sum(a)
count = 0
for i in a:
    if total_n % 2 == 0:
        if i % 2 == 0:
            count += 1
    else:
        if i % 2 == 1:
            count += 1
print(count)