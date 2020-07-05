

def isUnimodal():
    n = input()
    arr = input()
    arr = [int(n) for n in arr.split(" ")]
    len_of_arr = len(arr)

    max_of_arr = max(arr)
    max_count = arr.count(max_of_arr)

    max_first_index = arr.index(max_of_arr)
    max_last_index = len_of_arr - 1 - list(reversed(arr)).index(max_of_arr)

    # print(max_first_index)
    # print(max_last_index)

    i = max_first_index
    while i < max_last_index:
        if arr[i] != max_of_arr:
            print("NO")
            return
        i += 1

    i = 0
    while i < max_first_index:
        if arr[i] >= arr[i + 1]:
            print("NO")
            return
        i += 1

    i = max_last_index
    while i < len_of_arr - 1:
        if arr[i] <= arr[i + 1]:
            print("NO")
            return
        i += 1

    print("YES")

isUnimodal()
