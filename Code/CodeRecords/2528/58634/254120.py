#基于快速排序

def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:#改为大于等于就是升序排序
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


a = [int(i) for i in input().replace("[","").replace("]","").replace(","," ").split(" ")]
quick_sort(a,0,len(a)-1)
print(a)
