def delete_odd(arr_odd):
    if len(arr_odd) == 0:
        return False
    arr_max = max(arr_odd)
    arr_odd.remove(arr_max)
    return True


def delete_even(arr_even):
    if len(arr_even) == 0:
        return False
    arr_max = max(arr_even)
    arr_even.remove(arr_max)
    return True


def sum_of_delete_even_first(arr_odd, arr_even):
    while True:
        if not delete_even(arr_even):
            return sum(arr_odd) + sum(arr_even)
        if not delete_odd(arr_odd):
            return sum(arr_odd) + sum(arr_even)


def sum_of_delete_odd_first(arr_odd, arr_even):
    while True:
        if not delete_odd(arr_odd):
            return sum(arr_odd) + sum(arr_even)
        if not delete_even(arr_even):
            return sum(arr_odd) + sum(arr_even)


def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    arr_odd = []
    arr_even = []
    for ele in arr:
        if ele % 2 == 1:
            arr_odd.append(ele)
        else:
            arr_even.append(ele)

    print(
          min(
              sum_of_delete_even_first(arr_odd[:], arr_even[:]),
              sum_of_delete_odd_first(arr_odd[:], arr_even[:])
              )
          )


func()
