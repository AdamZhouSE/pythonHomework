def s9():
    array = []

    def permutations(arr, position, end):
        if position == end:
            array.append(list(arr))
        else:
            for index in range(position, end):
                arr[index], arr[position] = arr[position], arr[index]
                permutations(arr, position+1, end)
                arr[index], arr[position] = arr[position], arr[index]

    nums = list(input())
    permutations(nums, 0, len(nums))
    import math

    for n in array:
        if n[0] == '0':
            continue
        num = ""
        for i in n:
            num = num + str(i)
        if math.log(int(num), 2) % 1 == 0:
            print("true")
            return
    print("false")


s9()