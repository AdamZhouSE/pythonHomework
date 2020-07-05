n = int(input())
a = [(int(i) - 1) for i in input().split()]

count = 0
i = 0
while i < n:
    max_ = a[i]
    while i <= max_:
        if a[i] > max_:
            max_ = a[i]
        if i == max_:
            i += 1
            break
        i += 1
    count += 1

print(count)