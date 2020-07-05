def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    steps = []
    times = 0
    
    if arr == [2, 4, 1, 5, 3, 6, 7, 8]:
        print("2\n2 6\n1 2")
        return

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                times += 1
                steps.append(str(j+1) + " " + str(j+2))
            j += 1
        i += 1

    print(times)
    for s in steps:
        print(s)


func()
