t = int(input())
for ind in range(t):
    li = input().split(" ")
    numN = int(li[0])
    numL = int(li[1])
    undo_edges = []
    color1 = []
    color2 = []
    for i in range(numL):
        li = input().strip().split(" ")
        undo_edges.append([int(li[0]), int(li[1])])
    while len(undo_edges) != 0:
        color1.append(undo_edges[0][0])
        color2.append(undo_edges[0][1])
        del(undo_edges[0])
        j = 0
        while j < len(undo_edges):
            done = False
            if undo_edges[j][0] in color1:
                done = True
                if undo_edges[j][1] not in color2:
                    color2.append(undo_edges[j][1])
            elif undo_edges[j][0] in color2:
                done = True
                if undo_edges[j][1] not in color1:
                    color1.append(undo_edges[j][1])

            if (not done) and undo_edges[j][1] in color1:
                done = True
                if undo_edges[j][0] not in color2:
                    color2.append(undo_edges[j][0])
            elif (not done) and undo_edges[j][1] in color2:
                done = True
                if undo_edges[j][0] not in color1:
                    color1.append(undo_edges[j][0])

            if done:
                del(undo_edges[j])
                j -= 1
            j += 1

    canDraw = True
    for i in range(1, numN+1):
        if i in color1 and i in color2:
            canDraw = False

    if canDraw:
        print("YES")
    else:
        print("NO")
