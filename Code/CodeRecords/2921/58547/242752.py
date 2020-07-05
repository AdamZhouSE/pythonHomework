def func():
    temp_arr = [int(x) for x in input().split()]
    size = [temp_arr[0], temp_arr[1]]
    addend = temp_arr[2]
    numbers = []
    i = 0
    while i < size[0]:
        temp_arr = [int(x) for x in input().split()]
        numbers += temp_arr
        i += 1

    times = 0
    target = round(sum(numbers) / len(numbers))
    # print(target)

    last = 0
    i = -1
    if target not in numbers:
        while True:
            # print("i: "+str(i))
            # print("target: "+str(target))
            if target + i in numbers:
                target += i
                break
            if abs(last) == abs(i):
                i = abs(i) + 1
            else:
                last = i
                i = -i

    # print(target)
    for number in numbers:
        if (number - target) % addend != 0:
            print(-1)
            return
        times += abs(number - target) / addend

    print(int(times))


func()
