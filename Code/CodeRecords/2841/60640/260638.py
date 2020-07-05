def calculate_v(array, judge):
    if len(array) == 1:
        return array[0]
    else:
        new_arr = []
        if judge:
            for ii in range(0, len(array)-1, 2):
                new_arr.append(array[ii] | array[ii+1])
            judge = False
            return calculate_v(new_arr, judge)
        else:
            for ii in range(0, len(array)-1, 2):
                new_arr.append(array[ii] ^ array[ii+1])
            judge = True
            return calculate_v(new_arr, judge)


inp = input().split(" ")
n, m = int(inp[0]), int(inp[1])
lent = pow(2, n)
arr = [int(x) for x in input().split(" ")]
for i in range(m):
    inp = input().split(" ")
    p, b = int(inp[0]), int(inp[1])
    arr[p-1] = b
    res = calculate_v(arr, True)
    print(res)
