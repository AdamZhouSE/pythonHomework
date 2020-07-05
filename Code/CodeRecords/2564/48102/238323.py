def clear_k():
    array = eval(input())
    k = int(input())
    x = int(input())
    temp = abs(x - array[0])
    index = 0
    for i in range(1, len(array), 1):
        if abs(array[i] - x) < temp:
            temp = abs(array[i] - x)
            index = i
    left = index - 1
    right = index + 1
    res = [array[index]]
    for i in range(k-1):
        if left == -1:
            res.append(array[right])
            right += 1
        elif right == len(array):
            res.insert(0, array[left])
            left -= 1
        elif left >= 0 and abs(array[left] - x) <= abs(array[right] - x):
            res.insert(0, array[left])
            left -= 1
        else:
            res.append(array[right])
            right += 1

    return res


print(clear_k())