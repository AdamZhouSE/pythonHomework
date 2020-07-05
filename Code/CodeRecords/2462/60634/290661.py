arr = list(eval(input()))
arr.insert(0,-1)
arr.append(-1)
i = 1
while i < len(arr) - 1:
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        print(i-1)
        break
    i += 1