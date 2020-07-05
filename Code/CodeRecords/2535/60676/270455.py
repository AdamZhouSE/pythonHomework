def reunion(arr):
    res = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            res += 1
    return res


if __name__ == '__main__':
    print(reunion(eval(input())))