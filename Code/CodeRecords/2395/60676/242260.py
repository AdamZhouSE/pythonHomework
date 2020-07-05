def replace(arr):
    for i in range(len(arr)-1):
        if arr[i] == 0 or arr[i] == '0':
            arr[i] = 0
            continue
        if arr[i] == arr[i+1]:
            arr[i] = 2*int(arr[i])
            arr[i+1] = 0
    return push_zeros(arr)


def push_zeros(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            new_arr.append(0)
        else:
            if 0 in new_arr:
                new_arr.insert(new_arr.index(0), arr[i])
            else:
                new_arr.append(arr[i])
    return new_arr


result = []
for i in range(int(input())):
    a = input()
    array = input().split()
    result.append(replace(array))
for i in range(len(result)):
    for j in range(len(result[i])-1):
        print(result[i][j], end=' ')
    print(result[i][len(result[i])-1])