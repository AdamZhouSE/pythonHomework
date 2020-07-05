import numpy as np


def string_distance(str1, str2):

    m = str1.__len__()
    n = str2.__len__()
    distance = np.zeros((m + 1, n + 1))

    for i in range(0, m + 1):
        distance[i, 0] = i
    for i in range(0, n + 1):
        distance[0, i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            distance[i, j] = min(distance[i - 1, j] + 1, distance[i, j - 1] + 1,
                                 distance[i - 1, j - 1] + cost)  

    return distance[m, n]


if __name__ == '__main__':
    a = input()
    b = input()
    result = int(string_distance(a, b))
    print(result)
