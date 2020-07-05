arr = eval(input())
arr = sorted(arr)
temp = arr[0]
lest = 1
record = 1
for i in range(1, len(arr)):
    if arr[i] - temp == 1:
        lest += 1
    else:
        lest = 1
    temp = arr[i]
    if lest > record:
        record = lest
print(record)
