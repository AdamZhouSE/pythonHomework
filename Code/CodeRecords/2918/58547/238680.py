def local_max(boxes, up_bound):
    boxes_higher = boxes[:]
    boxes_lower = []

    i = 0
    while i < len(boxes):
        if boxes[i] < up_bound - 1:
            boxes_higher.remove(boxes[i])
            boxes_lower.append(boxes[i])
        i += 1

    # print("BBB: "+str(boxes)+" "+str(boxes_higher)+" "+str(boxes_lower))

    if len(boxes_higher) == 0:
        # print("lower: "+str(max(boxes_lower)) + " ub: " + str(up_bound))
        return max(boxes_lower)
    else:
        # print("higher: "+str(min(boxes_higher)) + " ub: " + str(up_bound))
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

        # 确定up_bound:
        i = 0
        min_up_bound = 99999
        while i < len(temp):
            temp_bound = temp[i] - (len(temp) - i) + 1
            if temp_bound < min_up_bound:
                min_up_bound = temp_bound
            i += 1
        # print("TEMP: "+str(temp))
        # print("TB: "+str(min_up_bound))
        now_max = local_max(boxes, min_up_bound)  # 传入容量
        if is_available(temp, now_max):
            temp.append(now_max)
            boxes.remove(now_max)
        else:
            heaps.append(temp)
            return


def func():
    n = int(input())
    boxes = [int(x) for x in input().split(" ")]
    # boxes = [int(x) for x in input()[1:-1].split(", ")]

    heaps = []
    while len(boxes) > 0:
        make_heap(heaps, boxes)
        # print("heaps: "+str(heaps))
        # print("boxes: "+str(boxes))
        # print("--------------------------")

    print(len(heaps))


func()
