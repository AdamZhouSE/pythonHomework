def quick_sort(lst, l, r):
    pivot = lst[r]
    i, j = l, r
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        while lst[j] > pivot and i < j:
            j -= 1
        while lst[i] <= pivot and i < j:
            i += 1
    lst[i], lst[l] = pivot, lst[i]
    if i > l + 1:
        quick_sort(lst, l, i - 1)
    if j < r - 1:
        quick_sort(lst, j + 1, r)


l_lst = eval(input())
quick_sort(l_lst, 0, len(l_lst) - 1)
print(l_lst)
