arr = eval(input())
for i in range(1, len(arr)):
    ele = arr[i]
    j = i-1
    while j >= 0:
        if arr[j] > ele:
            arr[j+1] = arr[j]
            arr = ele
        j -= 1
print(arr)
