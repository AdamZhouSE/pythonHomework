
def func4():
    arr, val, res = eval(input()), 0, []
    for i in range(0, len(arr)):
        if res.count(arr[i][1]) > 0:
            val = i
        else:
            res.append(arr[i][1])
    print(arr[val])


func4()
