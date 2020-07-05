arr = eval(input())
max = 1
temp = arr[0]
record = 1
for i in arr:
    if i > temp:
        max += 1
        if max >record:
            record = max
    else:
        max = 1
    temp = i
print(record)
