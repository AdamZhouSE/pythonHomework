number = input().split()
temp = input().split()
array = []
for item in temp:
    array.append([-1, int(item)])
for i in range(int(number[0]) - 1):
    temp = input().split()
    u = int(temp[0]) - 1
    v = int(temp[1]) - 1
    array[v][0] = u
for i in range(int(number[1])):
    temp = input().split()
    if temp[0] == '1':
        x = int(temp[1]) - 1
        a = int(temp[2])
        array[x][1] = array[x][1] + a
    elif temp[0] == '2':
        x = int(temp[1]) - 1
        a = int(temp[2])
        for j in range(len(array)):
            end = j
            while end >= 0:
                if end == x:
                    array[j][1] = array[j][1] + a
                    break
                end = array[end][0]
    else:
        x = int(temp[1]) - 1
        count = 0
        while x != -1:
            count = count + array[x][1]
            x = array[x][0]
        print(count)