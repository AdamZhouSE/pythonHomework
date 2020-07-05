arr = list(eval(input()))

Min = arr[len(arr)-1]

i = len(arr)-1
while i >= 0:
    if arr[i] < Min:
        Min = arr[i]
    if i >= 1 and arr[i-1] > arr[i]:
        break
    i -= 1
    
print(Min)