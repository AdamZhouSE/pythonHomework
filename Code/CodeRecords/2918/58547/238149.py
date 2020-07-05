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
        now_max = max(boxes)
        if is_available(temp, now_max):
            temp.append(now_max)
            boxes.remove(now_max)
        else:
            heaps.append(temp)
            return


def func():
    n = int(input())
    boxes = [int(x) for x in input().split(" ")]

    heaps = []
    while len(boxes) > 0:
        make_heap(heaps, boxes)

    print(len(heaps))


func()
