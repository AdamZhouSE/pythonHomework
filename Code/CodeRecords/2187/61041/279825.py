numberOfEx = int(input())
for i in range(0,numberOfEx):
    x = input()
    y = input()
    num_x = []
    value = ''
    for i in range(0, len(x)):
        if x[i] != " ":
            value = value + x[i]
            continue
        else:
            num_x.append(value)
            value = ''
    num_x.append(value)
    value = ''
    num_y = []
    value = ''
    for i in range(0, len(y)):
        if y[i] != " ":
            value = value + y[i]
            continue
        else:
            num_y.append(value)
            value = ''
    num_y.append(value)
    value = ''

    index = int(num_x[0])
    number = int(num_x[1])
    maxValue = 0
    v = 0
    for i in range(0,index - number + 1):
        for j in range(0,number) :
            v = v + int(num_y[i+j])
        if v >= maxValue :
            maxValue = v
        v = 0
    print(maxValue)