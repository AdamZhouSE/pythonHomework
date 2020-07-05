def is_ass(ele, index, arr):
    i = 0
    while i < len(arr):
        if len(ele) == 0:
            return True

        if i == index:
            i += 1
            continue

        if ele.startswith(arr[i]):
            if is_ass(ele[len(arr[i]):], index, arr):
                return True

        i += 1

    return False


def func():
    arr = input()[2:-2].split("\",\"")
    asses = []
    i = 0
    while i < len(arr):
        if is_ass(arr[i], i, arr):
            asses.append(arr[i])
            arr.pop(i)
            continue
        i += 1

    print(asses)


func()
