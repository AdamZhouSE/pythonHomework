arr = list(map(int, input().split(",")))
record = []
for i in range(len(arr)):
    temp = 1
    for j in range(i):
        if arr[j] < arr[i]:
            if record[j] >= temp:
                temp = record[j]+1
    record.append(temp)
print(max(record))