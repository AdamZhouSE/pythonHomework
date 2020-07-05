nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
value = list(map(int, input().split()))
for i in range(m):
    instruction = list(map(int, input().split()))
    code = instruction[0]
    x = instruction[1]
    y = instruction[2]
    if code == 1:
        k = instruction[3]
        for j in range(x-1, y):
            value[j] = value[j] + k
    elif code == 2:
        result = sum(value[x-1:y])/(y-x+1)
        print('%.4f' % result)
    else:
        temp = sum(value[x-1:y])/(y-x+1)
        s = 0
        for j in value[x-1:y]:
            s = s + pow((j-temp), 2)
        result = s/(y-x+1)
        print('%.4f' % result)