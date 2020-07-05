str = input()  # [3,6,9,91]
str = str[1:len(str)-1]
li = str.split(",")
arr = []
for item in li:
    arr.append(int(item))

arr.sort()
result = 0
if len(arr) >= 2:
    i = 0
    diff = []
    while i < len(arr) - 1:
        diff.append(int(arr[i + 1]) - int(arr[i]))
        i += 1
    result = max(diff)
print(result)
