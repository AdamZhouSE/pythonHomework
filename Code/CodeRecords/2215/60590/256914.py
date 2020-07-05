lists = list(map(int, input().split(",")))

def optimizeDivision(arr):
    length = len(arr)

    if length == 1:
        return str(arr[0])
    elif length == 2:
        return str(arr[0])+"/"+str(arr[1])
    res = ""
    for i in range(length):
        if i == 0:
            res = res + str(arr[i]) + "/("
        elif i == length-1:
            res = res + str(arr[i]) +")"
        else:
            res = res + str(arr[i]) + "/"
    return res

print(optimizeDivision(lists))