n = eval(input())
box = sorted(list(map(int, input().split(' '))))
heap = 0
while len(box) > 0:
    count = 0
    i = 0
    size = len(box)
    while i < size:
        if box[i] >= count:
            box.pop(i)
            count += 1
            size -= 1
        else:
            i += 1
    heap += 1
print(heap)
