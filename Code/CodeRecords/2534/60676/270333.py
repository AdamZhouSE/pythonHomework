def merge(nums_list):
    res = []
    heap = []
    for i in range(len(nums_list)):
        heap.append(nums_list[i][0])
    while len(heap) > 0:
        res.append(min(heap))
        index = heap.index(res[-1])
        if len(nums_list[index]) > 1:
            nums_list[index].remove(nums_list[index][0])
            heap[index] = nums_list[index][0]
        else:
            nums_list = nums_list[:index] + nums_list[index+1:]
            heap = heap[:index] + heap[index+1:]
    return res


if __name__ == '__main__':
    print(merge(eval(input())))