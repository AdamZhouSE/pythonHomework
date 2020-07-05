import queue
def rearrangeBarcodes(barcodes):
    n = len(barcodes)
    que = queue.PriorityQueue()
    tmp = {}
    for i in barcodes:
        if i not in tmp:
            tmp[i] = 1
        else:
            tmp[i] += 1
    for key in tmp:
        que.put([-tmp[key], key])
    res = []
    if que.qsize():
        se = que.get()
        res.append(se[1])
        se[0] += 1
    while que.qsize():
        it = que.get()
        res.append(it[1])
        it[0] += 1
        if se[0]:
            que.put(se)
        se = it
    return res


listStr=input()
listStr=listStr[1:len(listStr)-1]
list=listStr.split(',')
numbers=[]
for c in list:
    numbers.append(int(c))
print(rearrangeBarcodes(numbers))