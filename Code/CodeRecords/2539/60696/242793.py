arr = [int(i) for i in input()[1:-1].split(', ')]
while True:
    if arr[-1] == max(arr):
        arr.pop(-1)
    else:
        break
while True:
    if arr[0] == min(arr):
        arr.pop(0)
    else:
        break
print(len(arr))