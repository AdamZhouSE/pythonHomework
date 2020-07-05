arr = [int(i) for i in input()[1:-1].split(',')]
count = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]>2*arr[j]:
            count += 1
print(count)