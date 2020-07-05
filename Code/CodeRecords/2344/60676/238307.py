def rotate_array(array, num):
    new_array = []
    for i in range(num, len(array)):
        new_array.append(array[i])
    for i in range(num):
        new_array.append(array[i])
    return new_array


result = []
for i in range(int(input())):
    line1 = input()
    line2 = input().split(' ')
    for j in range(len(line2)):
        line2[j] = int(line2[j])
    result.append(rotate_array(line2, int(input())))
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()