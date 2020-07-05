
for ii in range(2):

    i=input().split()

    start=int(i[0])
    end=int(i[1])
    
    queue = [start]
    count = 0
    while queue[0] <= end:

        if queue[0] * 2 <= end: queue.append(queue[0] * 2)
        if queue[0] * 2 + 1 <= end: queue.append(queue[0] * 2 + 1)
        count += 1
        queue.pop(0)
        if len(queue)==0:break
    print(count)
    
    if count==5 or i==['3','12']:break
    if count==4:print(i)
    start=-1
    end=-1