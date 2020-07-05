arr = list(eval(input()))

h = 0
i = len(arr) - 1
while i >= 0:
    if arr[i] > h:
        h += 1
    else:
        break
    i -= 1


print(h)