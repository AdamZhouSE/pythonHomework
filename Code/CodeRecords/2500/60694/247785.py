def pancakeSort(arr):
    '''
    思路：
    每次循环找到最大值的位置，然后将其翻转到列表首位，
    再翻转待排序的子列表长度，将它翻转到列表最后（次后、次次后...）的位置。
    每次循环待排数减1
    '''
    ans = []
    length = len(arr)
    while length > 1:
        max_pos = arr.index(max(arr[:length]))
        if max_pos != 0:  # 最大值不是第一个元素时要翻转2次
            arr = arr[max_pos::-1] + arr[max_pos + 1:]
            arr = arr[length - 1::-1] + arr[length:]
            ans += [max_pos, length]
        else:  # 否则翻转当前未排序长度即可
            ans += [length]
        length -= 1

    return ans


arr = eval(input())
print(pancakeSort(arr))
