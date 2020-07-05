def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]

    t = arr[:]
    lights_to_off = 0

    i = 1
    while i < n - 1:
        if arr[i-1] == 1 and arr[i+1] == 1 and arr[i] == 0:
            # troubled
            if i - 3 > 0 and arr[i-2] == 0 and arr[i-3] == 1:
                lights_to_off += 1
                arr[i - 1] = 0  # turn off
            elif i + 2 < n and arr[i+2] == 0 and arr[i+3] == 1:
                lights_to_off += 1
                arr[i + 1] = 0  # turn off
            else:
                lights_to_off += 1
                arr[i - 1] = 0  # turn off left lights by default
        i += 1

    print(lights_to_off)


func()
