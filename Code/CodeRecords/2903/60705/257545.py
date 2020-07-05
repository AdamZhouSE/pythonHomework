def contains_duplicate(string):
    for i in range(1, len(string)):
        if string[i] in string[0:i-1]:
            return True
    return False


def contains_duplicate_2(string1, string2):
    for i in range(0, len(string2)):
        if string2[i] in string1:
            return True
    return False


if __name__ == '__main__':
    # print(contains_duplicate("un"))
    arr = input()[1:-1].split(",")
    for i in range(0, len(arr)):
        arr[i] = arr[i][1:-1]
    i = 0
    while i < len(arr):
        if contains_duplicate(arr[i]):
            del(arr[i])
            i -= 1
        i += 1

    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if contains_duplicate_2(arr[i], arr[j]):
                if len(arr[i]) <= len(arr[j]):
                    del(arr[i])
                else:
                    del(arr[j])
                i = -1
                break
            j += 1
        i += 1

    l = 0
    for i in range(0, len(arr)):
        l += len(arr[i])
    print(l)