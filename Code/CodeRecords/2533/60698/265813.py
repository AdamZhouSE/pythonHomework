# 29
arr = list(eval(input()))
i = 0
n=len(arr)
count=0
while i < len(arr) and count<n:
    if arr[i] % 2 != 0:
        arr.append(arr[i])
        arr.pop(i)
        i = i - 1
    i = i + 1
    count=count+1
print(arr)