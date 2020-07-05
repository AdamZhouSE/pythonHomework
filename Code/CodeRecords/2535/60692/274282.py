a = input()[1:-1].split(",")
a = [int(i) for i in a]
count = 1
i = 0
j = i + 1
while j < len(a):
    if a[j] > max(a[i:j]):
        count += 1
        i = j
    j += 1
print(count)