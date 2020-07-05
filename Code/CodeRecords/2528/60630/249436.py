def qSort(lst, left, right) :
    mid = lst[(left + right) >> 1]
    i = left ; j = right
    while i < j :
        while lst[i] < mid :
            i += 1
        while lst[j] > mid :
            j -= 1
        if i <= j :
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            i += 1 ; j -= 1
    if i < right :
        qSort(lst, i, right)
    if j > left :
        qSort(lst, left, j)

num = [int(p) for p in input("")[1 : -1].split(',')]
qSort(num, 0, len(num) - 1)
print(num)
