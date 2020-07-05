def func15():
    arr, pairs, i = list(input()), sorted(eval(input()), key=lambda x: x[0]), 0
    while i < len(pairs):
        if ord(arr[pairs[i][0]]) > ord(arr[pairs[i][1]]):
            t = arr[pairs[i][0]]
            arr[pairs[i][0]] = arr[pairs[i][1]]
            arr[pairs[i][1]] = t
            i = 0
        else:
            i += 1
    print("".join(arr))


func15()
