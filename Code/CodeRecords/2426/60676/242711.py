def get_best(arr):
    for i in range(len(arr)):
        if int(arr[i]) >= 0:
            arr[i] = int(arr[i])
        else:
            arr[i] = -int(arr[i])
    arr.sort()
    return arr[-1] * arr[-2] * arr[-3]


result = []
for i in range(int(input())):
    a = input()
    array = input().split()
    result.append(get_best(array))
for i in range(len(result)):
    print(result[i])