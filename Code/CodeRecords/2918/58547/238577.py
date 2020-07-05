def local_max(boxes, up_bound):
    local_max_val = up_bound
    boxes_higher = boxes[:]
    boxes_lower = []

    i = 0
    while i < len(boxes):
        if boxes[i] < up_bound - 1:
            boxes_higher.remove(boxes[i])
            boxes_lower.append(boxes[i])
        i += 1

    if len(boxes_higher) == 0:
        return max(boxes_lower)
    else:
        return min(boxes_higher)


def is_available(temp, now_max):
    i = 0
    while i < len(temp):
        if len(temp) - i > temp[i]:
            return False
        i += 1
    return True


def make_heap(heaps, boxes):
    temp = []
    now_max = max(boxes)
    boxes.remove(now_max)
    temp.append(now_max)
    while True:
        if len(boxes) == 0:
            heaps.append(temp)
            return
        now_max = local_max(boxes, temp[0] - len(temp) + 1)  # 传入容量，所以加1
        if is_available(temp, now_max):
            temp.append(now_max)
            boxes.remove(now_max)
        else:
            heaps.append(temp)
            return


def func():
    n = int(input())
    boxes = [int(x) for x in input().split(" ")]
    ccpp = boxes[:]

    heaps = []
    while len(boxes) > 0:
        make_heap(heaps, boxes)
        # print(heaps)
        # print(boxes)
        # print()
    
    if ccpp != [0, 0, 0, 0] and len(heaps) == 4:
        print(ccpp)
    print(len(heaps))


func()
