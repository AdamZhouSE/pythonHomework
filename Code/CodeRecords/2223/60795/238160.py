arr=raw_input().split(',')
le = len(arr)
for i in range(0, le):
    arr[i] = int(arr[i])
re = 0
new = -4
for i in range(0, le):
    for j in range(i + 1, le):
        if arr[i] >arr[j]:
           arr[i], arr[j] = arr[j], arr[i]
for j in range(0, le):
    for k in range(j + 1, le):
        if arr[k] == arr[j]:
           re = arr[j]
           if arr[j] == j + 1:
              new = arr[k - 1] + 1
           else:
              new = j + 1
           break
list = [re, new]
print(list)