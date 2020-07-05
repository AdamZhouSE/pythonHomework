arr = list(eval(input()))
arr.sort()
t = -1
i = 0
while i < len(arr)-1:
    if arr[i] == arr[i+1]:
        t = arr[i]
        break
    i += 1
print(t)