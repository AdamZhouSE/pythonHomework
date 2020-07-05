arr = list(map(int, input().split(",")))
up = True
found = False
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        if up:
            print(i)
            found = True
            break
        else:
            up = False
    elif arr[i] < arr[i + 1]:
        up = True
    else:
        up = False
if not found:
    print(len(arr) - 1)
