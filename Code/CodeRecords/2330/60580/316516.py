import itertools
import math

num = int(input())
array = [[0 for _ in range(2)] for _ in range(num)]
for i in range(num):
    temp = input().split(',')
    array[i][0] = int(temp[0])
    array[i][1] = int(temp[1])


def manage(array, num):
    ans = float("inf")
    for p1, p2, p3 in itertools.combinations(array, 3):
        p4 = [p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]]
        if p4 in array:
            temp = (p2[0] - p1[0]) * (p3[0] - p1[0]) + (p2[1] - p1[1]) * (p3[1] - p1[1])
            if temp == 0:
                length1 = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
                length2 = math.sqrt((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2)
                area = length1 * length2
                if area < ans:
                    ans = area
    return ans


result = manage(array, num)
if result == float("inf"):
    print("0.0000")
else:
    print("%.4f" % result)
