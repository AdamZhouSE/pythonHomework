str = input()
str = str[1:len(str)-1]
arr = str.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
arr.sort()

for i in range(len(arr)):
    if arr[i]>0:
        arr = arr[i:]
        break
missing = len(arr)+1
for i in range(len(arr)):
    if arr[i]!=i+1:
        missing = i + 1
        break
print(missing)