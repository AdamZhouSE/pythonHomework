def max_prob(arr, cursor):
    length_of_arr = len(arr)
    i = cursor
    max_prob_len = 0
    while i < length_of_arr - 1:
        if i == cursor:
            max_prob_len += 1
            i += 1
            continue
        if arr[i+1] <= arr[i] * 2:
            max_prob_len += 1
        else:
            break
        i += 1
    return max_prob_len


def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    max_prob_len = 0

    i = 0
    while i < n - max_prob_len:
        now_len = max_prob(arr, i)
        if now_len > max_prob_len:
            max_prob_len = now_len
        i += 1

    print(max_prob_len)


func()
