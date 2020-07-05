def swap(x, y, array):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def filter(i,array):
    i -= 1
    while i >= 0:
        if array[i] >= array[i + 1]:
            break
        swap(i, i + 1, array)
        i -= 1

def manage(p, point, k, array):
    if point == k:
        if array[k-1] < array[p]:
            swap(k-1,p,array)
            filter(k-1,array)
    else:
        point += 1
        swap(point, p, array)
        filter(point,array)
    return point


problems = int(input())
for p in range(problems):
    temp = input().split(" ")
    size = int(temp[0])
    k = int(temp[1])
    array = input().split(" ")

    point = -1
    i = 0
    while i < size:
        array[i] = int(array[i])
        point = manage(i, point, k, array)
        i += 1
    i = 0
    while i < k:
        print(array[i], end=" ")
        i += 1
    print()
