def s4():
    array = list(input().split(','))
    for i in range(len(array)):
        array[i] = int(array[i])
    add = []

    for i in range(len(array)):
        for j in range(i+1, len(array)+1):
            s = 0
            for t in range(i, j):
                s += array[t]
            add.append(s)
    print(max(add))

    
s4()