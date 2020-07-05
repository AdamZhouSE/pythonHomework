arr = list(eval(input()))
arr.sort()
Max = 0
long = 1
i = 1
while i < len(arr):
    if arr[i] == arr[i-1] + 1:
        long += 1
    else:
        if long > Max:
            Max = long
        long = 1
    i += 1
print(Max)