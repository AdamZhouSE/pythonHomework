def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        length = int(input())
        arr = [int(x) for x in input().split()]

        arr.sort()

        costs = 0
        while len(arr) > 1:
            arr[1] = arr[0] + arr[1]
            arr.pop(0)
            costs += arr[0]
            j = 0
            while j < len(arr) - 1:
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                else:
                    break
                j += 1

        print(costs)

        i += 1


func()
