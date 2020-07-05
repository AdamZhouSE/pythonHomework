def possible_triangles(array):
    if len(array) < 3:
        return 0
    else:
        count = 0
        for i in range(len(array)-2):
            for j in range(i+1, len(array)-1):
                for k in range(j+1, len(array)):
                    if int(array[i]) + int(array[j]) > int(array[k]):
                        count += 1
        return count


num = int(input())
res = []
for i in range(num):
    size = int(input())
    array = input().split(' ')
    for j in range(size):
        array[j] = int(array[j])
    array.sort()
    res.append(possible_triangles(array))
for i in range(num):
    print(res[i])