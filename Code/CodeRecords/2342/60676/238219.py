import math


def reverse_array(array, num):
    new_array = []
    for i in range(0, len(array), num):
        for j in range(min(num, len(array)-i)):
            new_array.append(array[i+min(num, len(array)-i)-j-1])
    return new_array


result = []
for i in range(int(input())):
    line1 = input().split(' ')
    line2 = input().split(' ')
    for j in range(len(line2)):
        line2[j] = int(line2[j])
    result.append(reverse_array(line2, int(line1[1])))
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()