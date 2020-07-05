def enqueue(data):
    queue.append(data)


def dequeue():
    result = queue[0]
    del (queue[0])
    return result


inputs = []
while True:
    try:
        inputs.append(input().strip())
    except EOFError as err:
        break
for l in inputs:
    if l == "0 0":
        continue
    li = l.strip().split(" ")
    end = int(li[1])
    nodes = [int(li[0])]
    queue = [int(li[0])]
    while True:
        x = dequeue()
        if x*2 < end:
            nodes.append(x*2)
            enqueue(x*2)
        elif x*2 == end:
            nodes.append(x*2)
            break
        else:
            break
        if x*2+1 < end:
            nodes.append(x*2+1)
            enqueue(x*2+1)
        elif x*2+1 == end:
            nodes.append(x*2+1)
            break
        else:
            break
    print(len(nodes))
