arr = list(input())
change = eval(input())
for i in change:
    temp = arr[i[0]]
    arr[i[0]] = arr[i[1]]
    arr[i[1]] = temp
print("".join(arr))
