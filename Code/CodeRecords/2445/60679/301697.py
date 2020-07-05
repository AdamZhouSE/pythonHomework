def sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j]>arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return(arr)

read = input()
s = read[read.index('s = "')+5:read.index('t = "')-3]
t = read[read.index('t = "')+5:len(read)-1]
arr_s = sort(list(s))
arr_t = sort(list(t))
s = "".join(arr_s)
t = "".join(arr_t)
if s==t:
    print("true")
else:
    print("false")