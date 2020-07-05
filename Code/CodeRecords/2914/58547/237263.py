def func():
    n = int(input())
    arr_a = [int(x) for x in input().split(" ")]
    arr_b = [int(x) for x in input().split(" ")]
    if arr_a == arr_b:
        print("YES")
        return
    if n == 1:
        print("NO")
        return

    arr_c = []
    i = 0
    while i < n:
        arr_c.append(arr_a[i] - arr_b[i])
        i += 1

    if len(set(arr_c)) == 1:
        print("YES")
        return

    if len(set(arr_c)) > 2:
        print("NO")
        return



    temp_list = list(set(arr_c))
    temp_list.remove(0)
    value = temp_list[0]
    first_peak = arr_c.index(value)
    last_peak = n - list(reversed(arr_c)).index(value)
    if last_peak - first_peak == 1:
        print("NO")
        return 
    if len(set(arr_c[first_peak: last_peak])) != 1:
        print("NO")
        return

    print("YES")


def entrance():
    n = int(input())
    i = 0
    while i < n:
        func()
        i += 1


entrance()
