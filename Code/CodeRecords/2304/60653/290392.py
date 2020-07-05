n, ro = map(int, input().split(' '))
lch = [0] *1000
rch = [0] *1000
for i in range(0, n):
    t = list(int(n) for n in input().split(' '))
    w = t[0]
    lch[w] = t[1]
    rch[w] = t[2]
queue = []
queue.append(ro)
last = ro
level = 1
print("Level " + str(level) + ' ' + ':', end='')
while queue:
    root = queue.pop(0)
    print(' ', end='')
    print(root, end='')
    if lch[root] != 0:
        nlast = lch[root]
        queue.append(lch[root])
    if rch[root] != 0:
        nlast = rch[root]
        queue.append(rch[root])
    if root == last and queue:
        last = nlast
        print()
        level += 1
        print("Level " + str(level) + ' ' + ":", end='')
print()
queue = []
queue.append(ro)
islr = True
last = ro
nlast = None
level = 1
print("Level " + str(level) + ' ' + "from left to right" + ':', end='')
while queue:
    if islr:
        root = queue.pop(0)
        print(' ', end='')
        print(root, end='')
        if lch[root] != 0:
            if nlast == None:
                nlast = lch[root]
            queue.append(lch[root])
        if rch[root] != 0:
            if nlast == None:
                nlast = rch[root]
            queue.append(rch[root])
    else:
        root = queue.pop()
        print(' ', end='')
        print(root, end='')
        if rch[root] != 0:
            if nlast == None:
                nlast = rch[root]
            queue.insert(0, rch[root])
        if lch[root] != 0:
            if nlast == None:
                nlast = lch[root]
            queue.insert(0, lch[root])
    if root == last and queue:
        print()
        islr = not islr
        last = nlast
        nlast = None
        level += 1
        if islr:
            print("Level " + str(level) + ' ' + "from left to right" + ':', end='')
        else:
            print("Level " + str(level) + ' ' + "from right to left" + ':', end='')
print()            