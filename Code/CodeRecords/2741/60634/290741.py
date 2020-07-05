arr = eval(input())
Max = 1
long = 1
i = 1
while i < len(arr):
    if arr[i] > arr[i-1]:
        long += 1
        if long > Max:
            Max = long
    else:
        long = 1
    i += 1

print(Max)















